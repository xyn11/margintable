from bs4 import BeautifulSoup
import requests
import csv

def getdata(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content,'html.parser')
        tables = list(soup.find_all('table', attrs={'class':"rwd-table"}))
        # get head of table
        head = []
        hds = tables[0].find_all('th')
        for hd in hds:
                head.append(hd.text)
        # get data of all tables 
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
        # build dictionary of month to number
        mon = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        d = dict(zip(mon, range(1, 13)))
        # split month and year, store in two row, change records data from string to int type
        for i in range(len(records)):
             tmp = []
             tmp.append(d[records[i][0][:3]])
             tmp.append(int(records[i][0][-2:]))
             for j in range(1, len(records[i])):
                     tmp.append(int(records[i][j].replace(',', '')))
             records[i] = tmp
        # modify head
        head = ['Month', 'Year'] + head[1:]
        # change records to chronological order
        l = [records[-1]]
        tmp = records[-1][1]
        re = []
        for r in records[::-1][1:]:
                if l[-1][1] == r[1]:
                        l.append(r)
                else:
                        re += l[::-1]
                        l = [r]
                        tmp = r[1]   
        re += l[::-1]
        return [head] + re

def output(filename, records):
        with open(filename, 'w', newline = '') as f:
                writer = csv.writer(f)
                writer.writerows(records)

url = 'http://www.finra.org/investors/margin-statistics'
records = getdata(url)
output('output.csv', records)
