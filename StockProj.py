#TODO: 1. Figure out how to isolate the end of day returns over a period of time.
#TODO: 2. Put returns into a list or dictionary
#TODO: 3. Calculate return in percentage over time, as well as std. dev
#TODO 3.5. Use matrix operations to set a given allocation of money multiplied by a given share price
#TODO: 4. Calculate return of equities in the asset class, then incorporate the interest rate to maximize sharpe ratio
#TODO: 4.5 Set up FRED API to access 3-mo T-Bill rate
#TODO: 5. Set-up menu allowing for input of tickers
#TODO: 6. Desired output: a percentage of allocation for each asset

from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tickers = ['AMD','AAPL','GE','INTC','PYPL']
rate = .0107
A = []
B = []

C = np.matrix('.2; .2; .2; .2; .2', dtype=float)
IR=np.matrix(rate, dtype=float)

for t in tickers:
##calls the API to get the data for the given ticker
#ticker=input('Enter ticker symbol: ')
    ts = TimeSeries(key='9KNGZS8C0M32Y3LG',output_format='pandas')
    data,meta_data =ts.get_daily(symbol=t,outputsize='compact')

    ##round about way but imports data as a DataFrame to allow me to turn it into a list, then an array next
    df = pd.DataFrame(data,columns=['date','open','high','low','close','volume'], dtype=np.float)

    #data.to_csv('dataframe.csv',header=['open','high','low','close','volume'], index=None,sep=',', mode='w',line_terminator='\n')
    #days=int(input(('Enter previous days return to calculate: '))

    ##assigns the dataframe as a csv for easier data manipulation offline and less time for the call

    ##isolates the "close" prices column for 25 days of returns
    listo=df.values[0:29,3]

    ##reverses the order of the array to correctly calculate the pct_change
    listochron=np.flipud(listo)

    ##calculates percentage change of the returns on a daily basis, the average of those, and the std. dev
    pct_change = np.diff(listochron) / listochron[:1]
    expec_return=np.mean(pct_change)
    std_return=np.std(pct_change)

    A.append(expec_return)
    B.append(std_return)
    matA=np.matrix(A, dtype=float)
    #print(matA,matA.shape)
    matB=np.matrix(B, dtype=float)
    #print(matB,matB.shape)

reward=np.dot(matA,C)
print(matA)
risk=np.dot(matB,C)
print(matB)
adj_reward=reward-IR
#print(adj_reward.shape)

#sharpemat=(int(np.dot(matA,C))-rate)/int((np.dot(matB,C)).getI())
sharpemat=np.dot((reward-IR),risk.getI())
print(type(sharpemat))
print(sharpemat)
sharpematDF=pd.DataFrame(sharpemat)

"""plt.plot(x=adj_reward, y=risk, title='Sharpe Ratio')
plt.plot(x=matA,y=matB,title='Sharpe Ratio')
plt.xlabel('Standard Deviation')
plt.ylabel('Expected Return')
plt.axis([0,1,0,2])
#plt.show()

#print(sharpemat)"""
