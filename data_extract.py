import bs4
import requests 

books_ny = []
authors_ny = []
publisher_ny = []
ny_times_urls = []

url = 'https://www.goodreads.com/book/title.xml?key={SYqVbtFBa5qkYRo1Q5qhQ}&title=The+Picture+of+Dorian+Gray'
r = requests.get(url)
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

#create a date range to loop through weeks
base_date = datetime.date(2018, 3, 25)

for i in range(53):
    if i == 0:
        ny_times_urls.append(base_date)
    else:
        ny_times_urls.append(ny_times_urls[i - 1] - datetime.timedelta(days=7))
        
 for i in range(len(ny_times_urls)):
    ny_times_urls[i] = 'https://www.nytimes.com/books/best-sellers/' + ny_times_urls[i].strftime('%Y/%m/%d') + '/combined-print-and-e-book-fiction/'

#gathering data from ny times
for url in ny_times_urls:
    r = requests.get(url) 
    r.raise_for_status()
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    try:
        for link in soup.find_all('h2', {'class':'title'}):
            ny_times_title.append(link.text)
            print('Downloading book title...')
            print()
    except:
        ny_times_title.append('No title found')
    try:
        for link in soup.find_all('p', {'class':'author'}):
            a = link.text
            a = a.split('by ')
            ny_times_author.append(a[1])
            print('Downloading book author...')
            print()
    except:
        ny_times_author.append('No author found')
    try:
        for link in soup.find_all('p', {'class':'publisher'}):
            ny_times_pub.append(link.text)
            print('Downloading book publisher...')
            print()
            try:
                for link in soup.find('div', {'class':'date-range tooltip'}):
                    ny_times_dates.append(link)
                    print('Adding date...')
                    print()
            except:
                ny_times_dates.append('No date found')
    except:
        ny_times_pub.append('No publisher found')
