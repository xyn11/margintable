import matplotlib.pyplot as plt
import pandas as pd

def plot(filename):
        # get dataframe
        records = pd.read_csv(filename)
        df = pd.DataFrame(records)
        # concatenate month and year, sum two credit accounts
        df['Month/Year'] = df['Month'].map(str) + '/' + df['Year'].map(str)
        df['SumCredit'] = df["Free Credit Balances in Customers' Cash Accounts"]\
                         + df["Free Credit Balances in Customers' Securities Margin Accounts"]
        # plot
        ax = df.plot(x = 'Month/Year', y = ["Debit Balances in Customers' Securities Margin Accounts",\
                         "Free Credit Balances in Customers' Cash Accounts",\
                         "Free Credit Balances in Customers' Securities Margin Accounts", "SumCredit"],\
                          style = ['ro', 'g^', 'b+', 'y*'], figsize = (25, 7))
        ax.set_ylabel('in millions')
        ax.set_title('Margin Statistics')
        fig = ax.get_figure()
        fig.savefig('plot.png')

plot('output.csv')