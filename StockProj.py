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

tickers = ['AMD','AAPL']
#tickers = ['AMD','AAPL','GE','INTC','PYPL']
for t in tickers:
##calls the API to get the data for the given ticker
#ticker=input('Enter ticker symbol: ')
    ts = TimeSeries(key='9KNGZS8C0M32Y3LG',output_format='pandas')
    data,meta_data =ts.get_daily(symbol=t,outputsize='compact')
    #data,meta_data =ts.get_daily(symbol='AMD',outputsize='compact')

    ##round about way but imports data as a DataFrame to allow me to turn it into a list, then an array next
    df = pd.DataFrame(data,columns=['date','open','high','low','close','volume'], dtype=np.float)
    #df=np.array(data[], dtype=np.float)

    #data.to_csv('dataframe.csv',header=['open','high','low','close','volume'], index=None,sep=',', mode='w',line_terminator='\n')

    #data.describe()
    #print(data)

    #listo=df.reset_index().values
    #listo=np.array(listo[0:30,3], dtype=np.float)

    #listo=df[0:25,['close']]
    # listo=df['close'].reset_index().values
    #listo=df.values.array([0:25,3],dtype=np.float)



    #days=int(input(('Enter previous days return to calculate: '))

    #a#ssigns the dataframe as a csv for easier data manipulation offline and less time for the call
    #df = pd.read_csv('dataframe.csv')
    ##isolates the "close" prices column for 25 days of returns
    listo=df.values[0:25,3]
    #listo.astype(float)
    ##reverses the order of the array to correctly calculate the pct_change
    listochron=np.flipud(listo)

    print(type(df))
    print(listo)
    print(listochron)
    print(listo.shape)

    ##calculates percentage change of the returns on a daily basis, the average of those, and the std. dev
    pct_change = np.diff(listochron) / listochron[:1]
    expec_return=np.mean(pct_change)
    std_return=np.std(pct_change)
    sharpe=(expec_return/std_return)

    print('expec_return of ' + t + '=')
    print(expec_return)
    print('std_return of ' + t + '=')
    print(std_return)


    ##MATRIX OPS

    A = [[]]
    np.concatenate((A,[[expec_return]]),1)
    B = [[]]
    np.concatenate((B,[[std_return]]),1)
    C = np.matrix('.1 .1 .1 .1 .1 .1 .1 .1 .1 .1')

    print(A,B,C)
