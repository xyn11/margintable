from bs4 import BeautifulSoup
import requests
import csv

def scrape_wensite(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,features="lxml")
    tmp = []
    price_box = soup.find('HistoricalPriceStore', attrs= {'class' : 'prices'})
    price = price_box.text
    tmp.append(price)
    return tmp

def output():
    with open('output.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow()

url = 'https://finance.yahoo.com/quote/%5EIXIC/history?p=%5EIXIC'
s = scrape_wensite(url)
print(s)