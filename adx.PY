import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

start_date = '2021-05-23'
end_date = '2023-05-23'
df = yf.download('INFY', start=start_date, end=end_date)

n = 14
df['TR'] = np.maximum(np.maximum(df['High'] - df['Low'], abs(df['High'] - df['Close'].shift())), abs(df['Low'] - df['Close'].shift()))
df['DMplus'] = np.where((df['High'] - df['High'].shift()) > (df['Low'].shift() - df['Low']), np.maximum(df['High'] - df['High'].shift(), 0), 0)
df['DMminus'] = np.where((df['Low'].shift() - df['Low']) > (df['High'] - df['High'].shift()), np.maximum(df['Low'].shift() - df['Low'], 0), 0)
ATR = df['TR'].rolling(n).mean()
DMplus = df['DMplus'].rolling(n).mean()
DMminus = df['DMminus'].rolling(n).mean()
DIplus = DMplus / ATR * 100
DIminus = DMminus / ATR * 100
df['DIplus'] = DIplus
df['DIminus'] = DIminus
DX = abs(DIplus - DIminus) / (DIplus + DIminus) * 100
adx = DX.rolling(n).mean()
df = df.assign(ADX = adx)

# Print results
df=df.drop(columns=["Adj Close","TR","DMplus","DMminus","Volume"])
print(df)

plt.plot(df.index, df.DIplus , color = 'green', label = 'DI+')
plt.plot(df.index, df.DIminus , color = 'red', label = 'DI-')
plt.plot(df.index, df.ADX , color = 'steelblue', label = 'ADX')
plt.xticks(rotation = 45,ha = 'right')
plt.legend()
plt.show()