import pandas as pd
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import seaborn as sns


req = requests.get(
    'https://www.iocl.com/Product_PreviousPrice/PetrolPreviousPriceDynamic.aspx')
content = req.content
soup = BeautifulSoup(content, 'lxml')
table = soup.find_all('table')
rows = soup.find('table').find('tbody').find_all('tr')
dates = []
delhi_prices = []
kolkata_prices = []
mumbai_prices = []
chennai_prices = []
petrol_prices = []
months_mapping = {"January": "01", "February": "02", "March": "03", 
                  "April": "04", "May": "05", "June": "06", "July": "07",
                  "August": "08", "September": "09", "October": "10",
                  "November": "11", "December": "12"}
for row in rows:
    cells = row.find_all('td')
    date = months_mapping[cells[0].get_text().replace('\n', '').split(',')[0]
                                  .split(' ')[0]]+'-'+cells[0].get_text()
                                  .replace('\n', '').split(',')[0]
                                  .split(' ')[1]+'-'+cells[0].get_text()
                                  .replace('\n', '').split(',')[1]
                                  .replace(' ', '')
    # print(date)
    delhi_price = cells[1].get_text().replace('\n', '')
    kolkata_price = cells[2].get_text().replace('\n', '')
    mumbai_price = cells[3].get_text().replace('\n', '')
    chennai_price = cells[4].get_text().replace('\n', '')
    # print(date)
    petrol_price = [date, delhi_price,kolkata_price, mumbai_price,
                    chennai_price]
    petrol_prices.append(petrol_price)

# print(petrol_prices)
# petrol_prices = [dates, delhi_prices, kolkata_prices, mumbai_prices, chennai_prices]
petrol_prices.pop(0)
df = pd.DataFrame(petrol_prices)
df.columns = ['dates', 'Delhi', 'Kolkata', 'Mumbai', 'Chennai']


print(df.head(100))
df.to_csv('petro.csv', index=False)
