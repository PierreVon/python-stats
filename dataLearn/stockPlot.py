import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# 日期,股票代码,名称,收盘价,最高价,最低价,开盘价,前收盘,涨跌额,涨跌幅,成交量,成交金额

span = 5000

a = np.loadtxt('000001.csv', dtype=np.float, delimiter=',', skiprows=31, usecols=(3, 9, 11), max_rows=span)
a = np.flipud(a)
df = pd.DataFrame(data=a)

date = np.loadtxt('000001.csv', dtype=np.str, delimiter=',', skiprows=1, usecols=0, max_rows=span)
dateFormat = [datetime.strptime(x, '%Y/%m/%d').date() for x in list(reversed(date))]


def status(x):
    return pd.Series([x.count(), x.min(), x.idxmin(), x.quantile(.25), x.median(),
                      x.quantile(.75), x.mean(), x.max(), x.idxmax(), x.mad(), x.var(),
                      x.std(), x.skew(), x.kurt()], index=['总数', '最小值', '最小值位置', '一四分位数',
                                                           '中位数', '三四分位数', '均值', '最大值', '最大值位数', '平均绝对偏差', '方差',
                                                           '标准差',
                                                           '偏度', '峰度'])


print(df.apply(status), '\n')

print(df[0].describe(), '\n')
print(df.describe(include='number'), '\n')  # describe by type

print(df.cov(), '\n')
print(df.corr(), '\n')

print(sum(np.where(np.abs(a[:, 1]) > 2, 1, 0)))
print(sum(np.where(a[:, 1] >= 0, 1, 0)))

color = 'pink'

plt.figure(figsize=(20, 10))
plt.subplot(311)
plt.plot(dateFormat, a[:, 0])
plt.axhline(3000, 0, span, color=color)
plt.subplot(312)
plt.plot(np.arange(0, span, 1), a[:, 1])
plt.axhline(2, 0, span, color=color)
plt.axhline(-2, 0, span, color=color)
plt.subplot(313)
plt.plot(np.arange(0, span, 1), a[:, 2])
plt.axhline(2e11, 0, span, color=color)
plt.savefig('stock.png')
plt.show()

