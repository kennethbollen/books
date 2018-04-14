#from data_extract import *
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import chardet
import datetime

with open('/Users/DELL/Google Drive/Data Analysis/df_books.csv', 'rb') as f:
    find = chardet.detect(f.read())

df_books = pd.read_csv('/Users/DELL/Google Drive/Data Analysis/df_books.csv', encoding=find['encoding'])
df_books['Best_Seller_Week'] = pd.to_datetime(df_books['Best_Seller_Week'])
df_books = df_books.set_index(df_books['Best_Seller_Week'])
df_books['count'] = 1

#seperate into years and summarize stats sum
pub_13_cnt = pd.DataFrame(df_books.loc[df_books.index.year == 2013,['Publisher','count']].groupby('Publisher')['count'].sum())
pub_14_cnt = pd.DataFrame(df_books.loc[df_books.index.year == 2014,['Publisher','count']].groupby('Publisher')['count'].sum())
pub_15_cnt = pd.DataFrame(df_books.loc[df_books.index.year == 2015,['Publisher','count']].groupby('Publisher')['count'].sum())
pub_16_cnt = pd.DataFrame(df_books.loc[df_books.index.year == 2016,['Publisher','count']].groupby('Publisher')['count'].sum())
pub_17_cnt = pd.DataFrame(df_books.loc[df_books.index.year == 2017,['Publisher','count']].groupby('Publisher')['count'].sum())
pub_18_cnt = pd.DataFrame(df_books.loc[df_books.index.year == 2018,['Publisher','count']].groupby('Publisher')['count'].sum())
pub_total_cnt = pd.DataFrame(df_books.groupby('Publisher')['count'].sum())

#seperate into years and summarize stats for ratings
pub_13_mean = pd.DataFrame(df_books.loc[df_books.index.year == 2013,['Publisher','ratings']].groupby('Publisher')['ratings'].mean())
pub_14_mean = pd.DataFrame(df_books.loc[df_books.index.year == 2014,['Publisher','ratings']].groupby('Publisher')['ratings'].mean())
pub_15_mean = pd.DataFrame(df_books.loc[df_books.index.year == 2015,['Publisher','ratings']].groupby('Publisher')['ratings'].mean())
pub_16_mean = pd.DataFrame(df_books.loc[df_books.index.year == 2016,['Publisher','ratings']].groupby('Publisher')['ratings'].mean())
pub_17_mean = pd.DataFrame(df_books.loc[df_books.index.year == 2017,['Publisher','ratings']].groupby('Publisher')['ratings'].mean())
pub_18_mean = pd.DataFrame(df_books.loc[df_books.index.year == 2018,['Publisher','ratings']].groupby('Publisher')['ratings'].mean())
pub_total_mean = pd.DataFrame(df_books.groupby('Publisher')['ratings'].mean())

#rename columns to their years, which will be used later when we merge
pub_13_cnt = pub_13_cnt.rename(columns={'count': 'yr_2013'})
pub_14_cnt = pub_14_cnt.rename(columns={'count': 'yr_2014'})
pub_15_cnt = pub_15_cnt.rename(columns={'count': 'yr_2015'})
pub_16_cnt = pub_16_cnt.rename(columns={'count': 'yr_2016'})
pub_17_cnt = pub_17_cnt.rename(columns={'count': 'yr_2017'})
pub_18_cnt = pub_18_cnt.rename(columns={'count': 'yr_2018'})
pub_total_cnt = pub_total_cnt.rename(columns={'count': 'total_5yrs'})

#rename columns to their years, which will be used later when we merge for mean ratings
pub_13_mean = pub_13_mean.rename(columns={'ratings': 'yr_2013'})
pub_14_mean = pub_14_mean.rename(columns={'ratings': 'yr_2014'})
pub_15_mean = pub_15_mean.rename(columns={'ratings': 'yr_2015'})
pub_16_mean = pub_16_mean.rename(columns={'ratings': 'yr_2016'})
pub_17_mean = pub_17_mean.rename(columns={'ratings': 'yr_2017'})
pub_18_mean = pub_18_mean.rename(columns={'ratings': 'yr_2018'})
pub_total_mean = pub_total_mean.rename(columns={'ratings': 'total_5yrs'})

#sort the values
pub_13_cnt = pub_13_cnt.sort_values(by='yr_2013', ascending=False)
pub_14_cnt = pub_14_cnt.sort_values(by='yr_2014', ascending=False)
pub_15_cnt = pub_15_cnt.sort_values(by='yr_2015', ascending=False)
pub_16_cnt = pub_16_cnt.sort_values(by='yr_2016', ascending=False)
pub_17_cnt = pub_17_cnt.sort_values(by='yr_2017', ascending=False)
pub_18_cnt = pub_18_cnt.sort_values(by='yr_2018', ascending=False)
pub_13_mean = pub_13_mean.sort_values(by='yr_2013', ascending=False)
pub_14_mean = pub_14_mean.sort_values(by='yr_2014', ascending=False)
pub_15_mean = pub_15_mean.sort_values(by='yr_2015', ascending=False)
pub_16_mean = pub_16_mean.sort_values(by='yr_2016', ascending=False)
pub_17_mean = pub_17_mean.sort_values(by='yr_2017', ascending=False)
pub_18_mean = pub_18_mean.sort_values(by='yr_2018', ascending=False)

#merge files
pub_yrs_cnt = pd.merge(pub_13_cnt, pub_14_cnt, how='left', left_index=True, right_index=True)
pub_yrs_cnt = pd.merge(pub_yrs_cnt, pub_15_cnt, how='left', left_index=True, right_index=True)
pub_yrs_cnt = pd.merge(pub_yrs_cnt, pub_16_cnt, how='left', left_index=True, right_index=True)
pub_yrs_cnt = pd.merge(pub_yrs_cnt, pub_17_cnt, how='left', left_index=True, right_index=True)
pub_yrs_cnt = pd.merge(pub_yrs_cnt, pub_18_cnt, how='left', left_index=True, right_index=True)
pub_yrs_cnt = pd.merge(pub_yrs_cnt, pub_total_cnt, how='left', left_index=True, right_index=True)
pub_yrs_mean = pd.merge(pub_13_mean, pub_14_mean, how='left', left_index=True, right_index=True)
pub_yrs_mean = pd.merge(pub_yrs_mean, pub_15_mean, how='left', left_index=True, right_index=True)
pub_yrs_mean = pd.merge(pub_yrs_mean, pub_16_mean, how='left', left_index=True, right_index=True)
pub_yrs_mean = pd.merge(pub_yrs_mean, pub_17_mean, how='left', left_index=True, right_index=True)
pub_yrs_mean = pd.merge(pub_yrs_mean, pub_18_mean, how='left', left_index=True, right_index=True)
pub_yrs_mean = pd.merge(pub_yrs_mean, pub_total_mean, how='left', left_index=True, right_index=True)

#change the na into zeros
pub_yrs_cnt = pub_yrs_cnt.fillna(value=0)
pub_yrs_mean = pub_yrs_mean.fillna(value=0)
#sort by total
pub_yrs_cnt = pub_yrs_cnt.sort_values(by='total_5yrs', ascending=False)
pub_yrs_mean = pub_yrs_mean.sort_values(by='total_5yrs', ascending=False)
#calculate the percentage changes by the year
pub_yrs_cnt['pct_chg_14'] = (pub_yrs_cnt['yr_2014'] - pub_yrs_cnt['yr_2013']) / pub_yrs_cnt['yr_2013']
pub_yrs_cnt['pct_chg_15'] = (pub_yrs_cnt['yr_2015'] - pub_yrs_cnt['yr_2014']) / pub_yrs_cnt['yr_2014']
pub_yrs_cnt['pct_chg_16'] = (pub_yrs_cnt['yr_2016'] - pub_yrs_cnt['yr_2015']) / pub_yrs_cnt['yr_2015']
pub_yrs_cnt['pct_chg_17'] = (pub_yrs_cnt['yr_2017'] - pub_yrs_cnt['yr_2016']) / pub_yrs_cnt['yr_2016']
pub_yrs_mean['pct_mean_chg_14'] = (pub_yrs_mean['yr_2014'] - pub_yrs_mean['yr_2013']) / pub_yrs_mean['yr_2013']
pub_yrs_mean['pct_mean_chg_15'] = (pub_yrs_mean['yr_2015'] - pub_yrs_mean['yr_2014']) / pub_yrs_mean['yr_2014']
pub_yrs_mean['pct_mean_chg_16'] = (pub_yrs_mean['yr_2016'] - pub_yrs_mean['yr_2015']) / pub_yrs_mean['yr_2015']
pub_yrs_mean['pct_mean_chg_17'] = (pub_yrs_mean['yr_2017'] - pub_yrs_mean['yr_2016']) / pub_yrs_mean['yr_2016']

#explore changes in user ratings of best seller books over the last 5 years

#filter on the type of books
books_date_fiction = df_books.loc[df_books['Type'] == 'fiction',:].groupby('Best_Seller_Week')['ratings'].mean()
books_date_non_fiction = df_books.loc[df_books['Type'] == 'non_fiction',:].groupby('Best_Seller_Week')['ratings'].mean()

#resample the dates from weekly to annual
books_date_fiction = books_date_fiction.resample('A').mean()
books_date_non_fiction = books_date_non_fiction.resample('A').mean()

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

def autolabel_plt(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')


#who are the top 10 publishers by number of best sellers?
top_10_pub = pub_yrs_cnt.head(10)   
bar_xlabel = []

for i in top_10_pub.index:
	bar_xlabel.append(i)

N = len(top_10_pub)
width = 0.35        
top_10 = plt.bar(bar_xlabel, top_10_pub['total_5yrs'], width, color='r')
plt.xlabel('Publishers')
plt.ylabel('Number of Best Sellers')
plt.title('Top 10 Publishers based on #of Best Sellers (last 5 years)')
plt.show()


#what is the difference between the number of best sellers in 2013 and 2017
top_10_delta = pd.Series((top_10_pub['yr_2017'] - top_10_pub['yr_2013'])/top_10_pub['yr_2013'])

ind = np.arange(N)
fig, ax = plt.subplots()
y13 = ax.bar(ind, top_10_pub['yr_2013'], width, color='r')
y17 = ax.bar(ind + width, split_test['yr_2017'], width, color='y')
ax.set_ylabel('Number of NY Times Best Sellers')
ax.set_xlabel('Publishers (2013 vs 2017')
ax.set_title('Change in Num of Best Sellers for Top 10 Publishers')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(bar_xlabel)

ax2 = ax.twinx()
line1 = ax2.plot(ax.get_xticks(), top_10_delta , linestyle='-', marker='o', color='b', linewidth=1.0)

vals = ax2.get_yticks()
ax2.set_yticklabels(['{:3.2f}%'.format(x*100) for x in vals])
ax2.set_ylabel('% Change')

ax.legend((rects1[0], rects2[0], line1[0]), ('2013', '2017', '% Change'))


autolabel(y13)
autolabel(y17)
plt.show()

#has this been a trend?
trend = top_10_pub.loc[:,['pct_chg_14','pct_chg_15', 'pct_chg_16', 'pct_chg_17']]
trend = trend.T
trend_xlabels = ['2014', '2015', '2016', '2017']

for i in top_10_pub.index:
    plt.plot(trend_xlabels, trend[i], linestyle='-', marker='o')
    
plt.xlabel('Years')
plt.ylabel('% Change')
plt.title('Changes in # of Best Sellers')
plt.legend(loc='best')
plt.show()

#has the quality of the books been going down?
top_10_ratings = pd.DataFrame(top_10_pub.index)
top_10_ratings = pd.merge(top_10_ratings, pub_yrs_mean, how='left', left_on='Publisher', right_index=True)
top_10_ratings = top_10_ratings.set_index('Publisher')
top_10_ratings = top_10_ratings[['yr_2013','yr_2014','yr_2015','yr_2016','yr_2017']]
top_10_ratings = top_10_ratings.T

ratings_xlabels = ['2013','2014','2015','2016','2017']
N = len(ratings_xlabels)
ind = np.arange(N)
width = 0.35
fig, ax = plt.subplots()
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(rating_xlabel)

for pub in top_10_ratings.columns:
    ax.plot(ax.get_xticks(), top_10_ratings[pub], linestyle='-', marker='o')

ax.set_xlabel('Years')
ax.set_ylabel('Average User Ratings')
ax.set_title('User Ratings for Publication Books over 5 years')
ax.legend(loc='best')


