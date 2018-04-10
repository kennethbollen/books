from data_extract import *
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
pub_yrs_cnt = pd.merge(pub_yrs_cnt, pub_total, how='left', left_index=True, right_index=True)
pub_yrs_mean = pd.merge(pub_13_mean, pub_14_mean, how='left', left_index=True, right_index=True)
pub_yrs_mean = pd.merge(pub_yrs_mean, pub_15_mean, how='left', left_index=True, right_index=True)
pub_yrs_mean = pd.merge(pub_yrs_mean, pub_16_mean, how='left', left_index=True, right_index=True)
pub_yrs_mean = pd.merge(pub_yrs_mean, pub_17_mean, how='left', left_index=True, right_index=True)
pub_yrs_mean = pd.merge(pub_yrs_mean, pub_18_mean, how='left', left_index=True, right_index=True)
pub_yrs_mean = pd.merge(pub_yrs_mean, pub_total, how='left', left_index=True, right_index=True)

#change the na into zeros
pub_yrs_cnt = pub_yrs_cnt.fillna(value=0)
pub_yrs_mean = pub_yrs_mean.fillna(value=0)
#sort by total
pub_yrs_cnt = pub_yrs_cnt.sort_values(by='total_5yrs', ascending=False)
pub_yrs_mean = pub_yrs_mean.sort_values(by='total_5yrs', ascending=False)
#calculate the percentage changes by the year
pub_yrs_cnt['pct_chg_15'] = (pub_yrs_cnt['yr_2015'] - pub_yrs_cnt['yr_2014']) / pub_yrs_cnt['yr_2014']
pub_yrs_cnt['pct_chg_16'] = (pub_yrs_cnt['yr_2016'] - pub_yrs_cnt['yr_2015']) / pub_yrs_cnt['yr_2015']
pub_yrs_cnt['pct_chg_17'] = (pub_yrs_cnt['yr_2017'] - pub_yrs_cnt['yr_2016']) / pub_yrs_cnt['yr_2016']
pub_yrs_mean['pct_mean_chg_15'] = (pub_yrs_mean['yr_2015'] - pub_yrs_mean['yr_2014']) / pub_yrs_mean['yr_2014']
pub_yrs_mean['pct_mean_chg_16'] = (pub_yrs_mean['yr_2016'] - pub_yrs_mean['yr_2015']) / pub_yrs_mean['yr_2015']
pub_yrs_mean['pct_mean_chg_17'] = (pub_yrs_mean['yr_2017'] - pub_yrs_mean['yr_2016']) / pub_yrs_mean['yr_2016']

#explore changes in user ratings of best seller books over the last 5 years

#filter on the type of books
books_date_fiction = books.loc[books['Type'] == 'fiction',:].groupby('Best_Seller_Week')['ratings'].mean()
books_date_non_fiction = books.loc[books['Type'] == 'non_fiction',:].groupby('Best_Seller_Week')['ratings'].mean()

#resample the dates from weekly to annual
books_date_fiction = books_date_fiction.resample('A').mean()
books_date_non_fiction = books_date_non_fiction.resample('A').mean()

#plot line graphs
plt.plot(books_date_fiction, linestyle='-', marker='o', color='r', linewidth=1.0)
plt.plot(books_date_non_fiction, linestyle='-', marker='o', color='b', linewidth=1.0)
plt.xlabel('2013 - 2018')
plt.ylabel('Averager User Ratings')
plt.title('NY Times Best Seller Books Average User Ratings')
plt.legend(loc='best')
plt.show()

