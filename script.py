from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import csv

def getdata(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    tables = list(soup.find_all('table', attrs={'class':"rwd-table"}))
    head = []
    hds = tables[0].find_all('th')
    for hd in hds:
            head.append(hd.text)
    records = []
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
    return (head, records)

def cleandata():
        def helper(data):
                res = data[:4]
                for i in range(4, len(data), 12):
                        res = data[i:i+12] + res
                return res

        def toint(data):
                for i in range(len(data)):
                        data[i] = int(data[i].replace(',', ''))
                return data

        months = []
        db = []
        fcc = []
        fcs = []
        for r in records:
                months.append(r[0])
                db.append(r[1])
                fcc.append(r[2])
                fcs.append(r[3])
        mth = helper(months)
        deb = toint(helper(db))
        cash = toint(helper(fcc))
        sec = toint(helper(fcs))
        return (mth, deb, cash, sec)

def plot(mth, deb, cash, sec):
        fig, ax =plt.subplots(figsize = (125, 7))
        ax.plot(mth, deb, 'ro', label = "Debit Balances in Customers' 'Securities Margin Accounts")
        ax.plot(mth, cash, 'g^', label = "Free Credit Balance in Customers Cash Accounts")
        ax.plot(mth, sec, 'b+', label = "Free Credit Balenca in Customers' Securities Margin Accounts")
        ax.xaxis.set_tick_params(rotation=70)
        ax.xaxis.set_major_locator(plt.MaxNLocator(14))
        plt.ylabel('in $millions')
        plt.xlabel('Year')
        plt.title('Margin Statistics')
        plt.legend()



def output(records):
    with open('output.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(records)

url = 'http://www.finra.org/investors/margin-statistics'
records = scrape_wensite(url)
output(records)