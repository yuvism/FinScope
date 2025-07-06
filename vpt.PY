import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

start_date = '2021-05-23'
end_date = '2023-05-23'
df = yf.download('INFY', start=start_date, end=end_date)

df['price_diff'] = df['Close'].diff()
df['vol_price_trend'] = df['Volume'] * df['price_diff'] / df['Close'].shift()
df = df.drop(columns = ["Adj Close"])

print(df)

plt.plot(df.index,df.price_diff, color = 'black', label = 'Price Difference')
plt.plot(df.index,df.vol_price_trend, color = 'steelblue', label = 'Volume Price Trend Indicator')
plt.xticks(rotation =45, ha = 'right')
plt.legend()
plt.show()