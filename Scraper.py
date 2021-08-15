import requests
from bs4 import BeautifulSoup

# URL to be scraped
url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'

# Get URL HTML
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

data = []

data_iterator = iter(soup.find_all('td'))

while True:
    try:
        country = next(data_iterator).text
        confirmed = next(data_iterator).text
        deaths = next(data_iterator).text
        continents = next(data_iterator).text

        #convert deaths and confirmed to integers
        data.append ((
            country,
            int(confirmed.replace(',', '')),
            int(deaths.replace(',', '')),
            continents
        ))

    except StopIteration:
        break

# sort data
data.sort(key = lambda row: row[1], reverse = True)

# create text table object
import texttable as tt
table = tt.Texttable()

# add empty row at beginning of headers
table.add_rows([(None, None, None, None)] + data)

# 'l' denotes left, 'c' denotes center,
# and 'r' denotes right
table.set_cols_align(('c', 'c', 'c', 'c')) 
table.header((' Country ', ' Number of cases ', ' Deaths ', ' Continent '))
 
print(table.draw())