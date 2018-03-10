import bs4
import requests 

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
