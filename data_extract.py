import bs4
import requests
import datetime
import time
import pandas as pd
import numpy as np

#lists used for goodreads
books_ny = []
authors_ny = []
publisher_ny = []
#lists used for ny times 
best_seller_week = []
ny_times_urls_fiction = []
ny_times_urls_non_fiction = []
ny_times_title_fiction = []
ny_times_author_fiction = []
ny_times_pub_fiction = []
ny_times_title_non_fiction = []
ny_times_author_non_fiction = []
ny_times_pub_non_fiction = []
ny_times_rank_non_fiction = []
ny_times_rank_fiction = []

ny_times_dates = []
#counter used to access the date list and apply the correct best selling week
counter = -1
#empty dictionary to capture the rating score
book_rating = {}

#create a date range to loop through weeks
base_date = datetime.date(2018, 4, 15)
print('Base date set as: {}'.format(base_date))

#create dates for 5 year/week range
print('Creating date range')
print()
for i in range(261):
    if i == 0:
        #the first date in the list is the base date and won't require time delta calulation
        best_seller_week.append(base_date)
    else:
        #if not base date then append url list with the previous date in the list - 7 days
        #for time delta to work it requires the format to be in datetime and therefore i can't add the rest of the url in the same loop
        best_seller_week.append(best_seller_week[i - 1] - datetime.timedelta(days=7))
    
print('Creating urls to loop through...')
print()
#alter the url list of dates into urls    
for i in range(len(best_seller_week)):
    #dates are converted into the a url format
    ny_times_urls_fiction.append('https://www.nytimes.com/books/best-sellers/' + best_seller_week[i].strftime('%Y/%m/%d') + '/combined-print-and-e-book-fiction/')
    ny_times_urls_non_fiction.append('https://www.nytimes.com/books/best-sellers/' + best_seller_week[i].strftime('%Y/%m/%d') + '/combined-print-and-e-book-nonfiction/')
            
#web scrap ny times best seller web pages for books that made the list in the last year
for url in ny_times_urls_fiction:
    r = requests.get(url) 
    r.raise_for_status()
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    #counter will be used to access the date list to correctly apply the best seller week
    counter += 1
    print('downloading fictions books from: {}'.format(url))
    print()
    try:
        for link in soup.find_all('h2', {'class':'title'}):
            ny_times_title_fiction.append(link.text)
            #using the book title to identify the book rank for that week, ranks are contained in unordered list
            for link_two in soup.find_all('ul', {'class': 'action-menu'}):
                for link_three in link_two.li:
                    try:
                        #if statement to find where the book title mathces the current book title in the loop
                        if link_three['data-title'] == link.text:
                            #append the identified rank to the list and convert from string to an integer
                            ny_times_rank_fiction.append(int(link_three['data-rank']))
                        #to ensure the dataframe has equal sized columns depsite missing values    
                        else:
                            ny_times_rank_fiction.append('missing')
                    #skip non rank extraneous data
                    except TypeError:
                        continue
            ny_times_dates.append(best_seller_week[counter])           
    except:
        ny_times_title_fiction.append('No title found')
    try:
        for link in soup.find_all('p', {'class':'author'}):
            a = link.text
            a = a.replace('by ', '')
            ny_times_author_fiction.append(a)
    except:
        ny_times_author_fiction.append('No author found')
    try:
        for link in soup.find_all('p', {'class':'publisher'}):
            ny_times_pub_fiction.append(link.text)
    except:
        ny_times_pub_fiction.append('No publisher found')

for url in ny_times_urls_non_fiction:
    r = requests.get(url) 
    r.raise_for_status()
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    #counter will be used to access the date list to correctly apply the best seller week
    counter += 1
    print('downloading non-fictions books from: {}'.format(url))
    print()
    try:
        for link in soup.find_all('h2', {'class':'title'}):
            ny_times_title_non_fiction.append(link.text)
            #using the book title to identify the book rank for that week, ranks are contained in unordered list
            for link_two in soup.find_all('ul', {'class': 'action-menu'}):
                for link_three in link_two.li:
                    try:
                        #if statement to find where the book title mathces the current book title in the loop
                        if link_three['data-title'] == link.text:
                            ny_times_rank_non_fiction.append(int(link_three['data-rank']))
                        #to ensure the dataframe has equal sized columns depsite missing values    
                        else:
                            ny_times_rank_non_fiction.append('missing')
                    #append the identified rank to the list and convert from string to an integer
                    except TypeError:
                        continue
            ny_times_dates.append(best_seller_week[counter])           
    except:
        ny_times_title_non_fiction.append('No title found')
    try:
        for link in soup.find_all('p', {'class':'author'}):
            a = link.text
            a = a.replace('by ', '')
            ny_times_author_non_fiction.append(a)
    except:
        ny_times_author_non_fiction.append('No author found')
    try:
        for link in soup.find_all('p', {'class':'publisher'}):
            ny_times_pub_non_fiction.append(link.text)
    except:
        ny_times_pub_non_fiction.append('No publisher found')
          
#Create a dataframe to contain all data
df_fiction = pd.DataFrame({'Title': ny_times_title_fiction, 'Author': ny_times_author_fiction, 'Publisher': ny_times_pub_fiction, 'Best_Seller_Week': ny_times_dates, 'Rank_Week': ny_times_rank_fiction, 'Type': 'fiction'})
df_non_fiction = pd.DataFrame({'Title': ny_times_title_non_fiction, 'Author': ny_times_author_non_fiction, 'Publisher': ny_times_pub_non_fiction, 'Best_Seller_Week': ny_times_dates, 'Rank_Week': ny_times_rank_non_fiction, 'Type': 'non_fiction'})
#Create a list of book titles to find their ratings
books = df_fiction['Title'].unique()
books = np.append(books, df_non_fiction['Title'].unique())

#web scrap GoodReads using their API
for book in books:
    #GoodReads API developer terms require that no request be made for any method more than once a second
    #delay request to GoodReads by 2 seconds
    time.sleep(2)
    try:
        #To use the API, replace the white space of the title string with a +
        url = 'https://www.goodreads.com/book/title.xml?key={SYqVbtFBa5qkYRo1Q5qhQ}&title=%s' % book.replace(' ','+')
        r = requests.get(url)
        soup = bs4.BeautifulSoup(r.text, 'lxml')
        print('Updating book rating dictionary...')
        for link in soup.find('average_rating'):
            book_rating[book] = link
    except:
        print('Could not retrive')

#convert the book dictionary into a dataframe to merge with df_books
df_ratings = pd.Series(book_rating, name='ratings')
df_ratings = pd.DataFrame(df_ratings)
#To extract only fiction ratings, merge on left
df_fiction = pd.merge(df_fiction, df_ratings, how='left', left_on= df_fiction['Title'], right_index=True)
#To extract only non fiction ratings, merge on left
df_non_fiction = pd.merge(df_non_fiction, df_ratings, how='left', left_on= df_non_fiction['Title'], right_index=True)

#convert the ratings from a string into a float
df_fiction['ratings'] = df_fiction['ratings'].astype('float')
df_non_fiction['ratings'] = df_non_fiction['ratings'].astype('float')

#concatnate the datasets for one source
book_list = [df_fiction, df_non_fiction]
df_books = pd.concat(book_list)
#fill na ratings with the average
df_books['ratings'] = df_books['ratings'].fillna(value=df_books['ratings'].mean())
#sort dataframe by date and ascending ratings
df_books = df_books.sort_values(by=['Best_Seller_Week', 'Type', 'ratings'], ascending=False)
#convert Best Seller Week into a datetime datatype attribute
df_books['Best_Seller_Week'] = pd.to_datetime(df_books['Best_Seller_Week'])

#Create a dataframe of books and the number of weeks they were on the best seller list
'''df_best_weeks = pd.Series(Counter(df_books['Title']), name='num_weeks')
df_best_weeks = pd.DataFrame(df_best_weeks)
#merge together the rating and best seller data
df_fiction = pd.merge(df_ratings, df_best_weeks, how='inner', left_index=True, right_index=True)'''

















