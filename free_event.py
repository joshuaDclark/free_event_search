# import libraries
import csv
from datetime import datetime
import urllib.request
from bs4 import BeautifulSoup

# specified url
quote_page = "https://www.charlotteonthecheap.com/category/charlotte-kids/"

# query website and return the html to the variable
page = urllib.request.urlopen(quote_page)

# parse the html with beautiful soup and store in variable soup
soup = BeautifulSoup(page, "html.parser")

events = soup.find_all('article')
print(events)

# open a csv file with append, so old data will not be erased

# with open('index.csv', 'a') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow([events, datetime.now()])
