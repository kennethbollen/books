import bs4
import requests
import datetime

#lists used for goodreads
books_ny = []
authors_ny = []
publisher_ny = []
#lists used for ny times 
best_seller_week = []
ny_times_urls = []
ny_times_title = []
ny_times_author = []
ny_times_pub = []
ny_times_dates = []
#counter used to access the date list and apply the correct best selling week
counter = -1    

'''
#url = 'https://www.goodreads.com/book/title.xml?key={SYqVbtFBa5qkYRo1Q5qhQ}&title=The+Picture+of+Dorian+Gray'
#r = requests.get(url)
r.raise_for_status()
soup = bs4.BeautifulSoup(r.text, 'lxml')

for link in soup.find('average_rating'):
  book_rating.append(link)


#Remove unrelated data when scraping book titles
web_site_ratings = ['did not like it', 'it was ok', 'liked it', 'really liked it', 'it was amazing', 'View this quote', 'Goodreads Home']
#book titles scraped off each page
book_titles = []

url = 'https://www.goodreads.com/shelf/show/fiction'
req = requests.get(url)
req.raise_for_status()
soup = bs4.BeautifulSoup(req.text)

#web scaping the book titles 
for link in soup.find_all('a'):
  try:
    #this ensures that when scaping the titles we only get information related to books
    if link['title'] not in web_site_rating:
      book_titles.append(link['title'])
    else:
      continue
  except:
    continue


#get best seller information from the New York times
url = 'https://www.nytimes.com/books/best-sellers/combined-print-and-e-book-fiction'
r = request.get(url)
r.raise_for_status()
soup = bs4.BeautifulSoup(r.text, 'lxml')

for link in soup.find_all('h2', {'class':'title'}):
    books_ny.append(link.text)
    
for link in soup.find_all('p', {'class':'author'}):
    a = link.text
    a = a.split('by ')
    authors_ny.append(a[1])
    
for link in soup.find_all('p', {'class':'publisher'}):
    publisher_ny.append(link.text)
    
#see previous weeks list url
for link in soup.find_all('div', {'class':'arrow-navigation '}):
    print(link.a['href'])
'''

#create a date range to loop through weeks
base_date = datetime.date(2018, 3, 25)
print('Base date set as: {}'.format(base_date))

#create dates for 52 week range
print('Creating date range')
print()
for i in range(53):
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
    ny_times_urls.append('https://www.nytimes.com/books/best-sellers/' + best_seller_week[i].strftime('%Y/%m/%d') + '/combined-print-and-e-book-fiction/')
            

#web scrap ny times best seller web pages for books that made the list in the last year
for url in ny_times_urls:
    r = requests.get(url) 
    r.raise_for_status()
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    #x will be used to access the date list to correctly apply the best seller week
    counter += 1
    try:
        print('Downloading book title...')
        print()
        print('Adding best seller date...')
        print()
        for link in soup.find_all('h2', {'class':'title'}):
            ny_times_title.append(link.text)
            #i need the best seller week to be added to the list by the same number of times there are book titles             
            ny_times_dates.append(best_seller_week[counter])
    except:
        print('No title found')
        print()
        ny_times_title.append('No title found')
    try:
        print('Downloading book author...')
        print()
        for link in soup.find_all('p', {'class':'author'}):
            a = link.text
            a = a.split('by ')
            ny_times_author.append(a[1])
    except:
        print('No author found...')
        print()
        ny_times_author.append('No author found')
    try:
        print('Downloading book publisher...')
        print()
        for link in soup.find_all('p', {'class':'publisher'}):
            ny_times_pub.append(link.text)
    except:
        print('No publisher found...')
        print()
        ny_times_pub.append('No publisher found')
