import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

start_date = '2021-05-23'
end_date = '2023-05-23'
df = yf.download('INFY', start=start_date, end=end_date)

window = 20
df['upper_channel'] = df['High'].rolling(window=window).max().shift(window-1)
df['lower_channel'] = df['Low'].rolling(window=window).min().shift(window-1)
df['middle_channel'] = (df['upper_channel'] + df['lower_channel']) / 2

print(df)

plt.plot(df.index , df.upper_channel, color = 'green', label = 'Upper Channel')
plt.plot(df.index , df.middle_channel , color = 'black', label = 'Middle Channel')
plt.plot(df.index , df.lower_channel, color = 'red' , label = 'Lower Channel')
plt.legend()
plt.show()


