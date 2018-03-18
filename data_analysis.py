from data_extract import *

fiction = pd.Series(df_fiction.groupby('Title')['ratings'].mean())
non_fiction = pd.Series(df_non_fiction.groupby('Title')['ratings'].mean())

fiction = np.array(fiction)
non_fiction = np.array(non_fiction)

#handle any NaNs and covnert to zero
fiction = np.nan_to_num(fiction)
non_fiction = np.nan_to_num(non_fiction)

#permutation sampling to simulate the hypothesis that fiction book ratings and non-fiction book ratings have identical probability distributions.
def permutation_sample(data1, data2):
    """Generate a permutation sample from two data sets."""

    # Concatenate the data sets: data
    data = np.concatenate((data1, data2))

    # Permute the concatenated array: permuted_data
    permuted_data = np.random.permutation(data)

    # Split the permuted array into two: perm_sample_1, perm_sample_2
    perm_sample_1 = permuted_data[:len(data1)]
    perm_sample_2 = permuted_data[len(data1):]

    return perm_sample_1, perm_sample_2

#generate a permutation replicate from the permutation sample
def draw_perm_reps(data_1, data_2, func, size=1):
    """Generate multiple permutation replicates."""

    # Initialize array of replicates: perm_replicates
    perm_replicates = np.empty(size)

    for i in range(size):
        # Generate permutation sample
        perm_sample_1, perm_sample_2 = permutation_sample(data_1, data_2)
        # Compute the test statistic
        perm_replicates[i] = func(perm_sample_1, perm_sample_2)

    return perm_replicates
  
 def diff_of_means(data_1, data_2):
    """Difference in means of two arrays."""

    # The difference of means of data_1, data_2: diff
    diff = np.mean(data_1) - np.mean(data_2)

    return diff

#Compute difference of mean ratings
empirical_diff_means = diff_of_means(fiction, non_fiction)

# Draw 10,000 permutation replicates: perm_replicates
perm_replicates = draw_perm_reps(fiction, non_fiction,
                                 diff_of_means, size=10000)

# Compute p-value: p
p = np.sum(perm_replicates >= empirical_diff_means) / len(perm_replicates)

# Print the result
print('same distribution p-value =', p)
#p-value = 0.493

#test the hypothesis that Frog A and Frog B have the same mean impact force

def bootstrap_replicate_1d(data, func):
    bs_sample = np.random.choice(data, len(data))
    return func(bs_sample)

#function to generate many bootstrap replicates from the data set
def draw_bs_reps(data, func, size=1):
    """Draw bootstrap replicates."""

    # Initialize array of replicates: bs_replicates
    bs_replicates = np.empty(size)

    # Generate replicates
    for i in range(size):
        bs_replicates[i] = bootstrap_replicate_1d(data, func)

    return bs_replicates

#concatenate the datasets
ratings_concat = np.concatenate((fiction, non_fiction))
#compute mean for all ratings
mean_ratings = np.mean(ratings_concat)

#shift both arrays to have the same mean as we are simulating the hypothesis that their means are equal
fiction_shifted = fiction - np.mean(fiction) + mean_ratings
non_fiction_shifted = non_fiction - np.mean(non_fiction) + mean_ratings

#draw bootstrap samples out of the shifted arrays and compute the difference in means
bs_replicates_fiction = draw_bs_reps(fiction_shifted, np.mean, size=10000)
bs_replicates_non_fiction = draw_bs_reps(non_fiction_shifted, np.mean, size=10000)
#calculate the bootstrap replicate
bs_replicates = bs_replicates_fiction - bs_replicates_non_fiction

#p-value is the fraction of replicates with a difference in means greater than or equal to what was observed
p = np.sum(bs_replicates >= empirical_diff_means) / len(bs_replicates)
print('same mean p-value =', p)
#p-value = 0.5087
