from data_extract import *
import pandas as pd
import matplotlib.pyplot as plt

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

