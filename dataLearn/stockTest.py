import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# a = np.loadtxt('000001.csv', dtype=np.float, delimiter=',', skiprows=1, usecols=(3,))
# print(a)
# plt.plot(np.arange(0, len(a)), list(reversed(a)))
# plt.show()

date = '日期'
maxPrice = '最高价'
finishPrice = '收盘价'
dealPrice = '成交金额'
amount = '成交量'
rate = '涨跌额'
df = pd.read_csv('000001.csv', sep=',')
period = 300
pot = False


def plotLine(col, pot):
    plt.title(col, fontproperties='Heiti TC', fontsize=10)
    plt.plot(dateFormat, list(reversed(df[col]))[df.__len__() - period:])
    if pot:
        plt.plot(dateFormat, list(reversed(df[col]))[df.__len__() - period:], 'mo', markersize=2)
    plt.axhline(np.average(np.array(list(reversed(df[col]))[df.__len__() - period:], dtype=np.float)), 0, period)


dateFormat = [datetime.strptime(x, '%Y/%m/%d').date() for x in list(reversed(df[date]))[df.__len__() - period:]]
plt.subplot(211)
plotLine(finishPrice, pot)

plt.subplot(212)
plotLine(amount, pot)

# plt.figure(figsize=(200, 150))
plt.show()
