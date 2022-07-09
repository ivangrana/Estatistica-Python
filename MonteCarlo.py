import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from pandas.plotting import register_matplotlib_converters
tabela_dados = pd.read_csv('AMZN.csv',header=0, usecols = ['Date','Close'],parse_dates=True,index_col='Date')

Data = tabela_dados.pct_change()

AmznLogReturns = np.log(1 + Data)
print(AmznLogReturns.tail(10))

# plt.figure(figsize=(10,5))
# plt.plot(AmznLogReturns)
# plt.show()

MeanLogReturns = np.array(AmznLogReturns.mean())
VarLogReturns = np.array(AmznLogReturns.var())
StdevLogReturns = np.array(AmznLogReturns.std())

Drift = MeanLogReturns - (0.5 * VarLogReturns)
print("Drift = ",Drift)

NumIntervals = 250
Iterations = 2

np.random.seed(7)

SBMotion = norm.ppf(np.random.rand(NumIntervals,Iterations))

DailyReturns = np.exp(Drift + StdevLogReturns * SBMotion)

StartStockPrices = Data.iloc[0]

StockPrice = np.zeros_like(DailyReturns)

StockPrice[0] = StartStockPrices

for t in range(1, NumIntervals):
 StockPrice[t] = StockPrice[t - 1] * DailyReturns[t]
 
plt.figure(figsize=(10,5))
AMZNTrend = np.array(Data.iloc[:, 0:1])
plt.plot(AMZNTrend,color = 'red')
plt.plot(SBMotion)

plt.show()