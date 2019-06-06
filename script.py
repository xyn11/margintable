from bs4 import BeautifulSoup
import requests
import csv

def scrape_wensite(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    records = []
    tables = list(soup.find_all('table', attrs={'class':"rwd-table"}))
    head = []
    hds = tables[0].find_all('th')
    for hd in hds:
            head.append(hd)
    for t in tables:
        tbody = t.find('tbody')
        rows = list(tbody.find_all('tr'))
        for r in rows:
                tds = r.find_all('td')
                re = []
                for td in tds:
                        re.append(td.text)
                if len(re) == len(head):
                        records.append(re)
    return records

def output(records):
    with open('output.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(records)

url = 'http://www.finra.org/investors/margin-statistics'
records = scrape_wensite(url)
