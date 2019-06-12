import matplotlib.pyplot as plt
import pandas as pd

def readdata(filename):
        records = pd.read_csv(filename)

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
        ax.plot(mth, deb, 'ro', label = "Debit Balances in Customers' Securities Margin Accounts")
        ax.plot(mth, cash, 'g^', label = "Free Credit Balance in Customers' Cash Accounts")
        ax.plot(mth, sec, 'b+', label = "Free Credit Balenca in Customers' Securities Margin Accounts")
        ax.xaxis.set_tick_params(rotation=70)
        ax.xaxis.(plt.MaxNLocator(14))
        plt.ylabel('in $millions')
        plt.xlabel('Month-Year')
        plt.title('Margin Statistics')
        plt.legend()