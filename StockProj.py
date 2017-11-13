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
from fred import Fred

#calls the API to get the data for the given ticker
#ticker=input('Enter ticker symbol: ')
ts = TimeSeries(key='9KNGZS8C0M32Y3LG',output_format='pandas')
data,meta_data =ts.get_daily(symbol='AMD',outputsize='compact')

#round about way but imports data as a DataFrame to allow me to turn it into a list, then an array next
df = pd.DataFrame(data)
#data.describe()

listo=df.values.tolist()
listo=np.array(listo[0:], dtype=np.float)

#days=int(input(('Enter previous days return to calculate: '))

#calculate mean, std dev of the first 0 - whatever rows in the 3rd column (close prices)
close_mean=np.mean(listo[0:25,3])
close_std=np.std(listo[0:25,3])

#beginning of the sharpe ratio that I'll use as one metric to optimize for the larger portfolio as a whole
sharpe=(close_mean/close_std)

print(listo[0:25,3])
print(close_mean)
print(close_std)
print(sharpe)
