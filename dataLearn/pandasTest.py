import pandas as pd
import numpy as np

print('# Series #')
print(pd.Series(range(3)))
print(pd.Series(np.arange(4), np.arange(6, 2, -1)))
print(pd.Series([3, 4, 5, 2, 6], index=['a', 'b', 'c', 'd', 'e']))
print(pd.Series({'a': 4, 'b': 8}))

d = pd.Series({'a': 4, 'b': 8})
print(d.values, d.index)
print(d['a'], d[0])
print(np.exp(d))
print('a' in d)
print(d.get('f', 20))
print(d * pd.Series([3, 4, 5, 2, 6], index=['a', 'b', 'c', 'd', 'e']))

print(d.name)
d.name = 'test'
d.index.name = 'index'
print(d)

print('\n# DataFrame #')
print(pd.DataFrame(np.arange(10).reshape(2, 5)))
print(pd.DataFrame({'a': pd.Series([1, 2, 3], index=['q', 'w', 'e']),
                    '测试': pd.Series([1, 2, 3], index=['q', 'w', 'e'])}))
d = pd.DataFrame([[1, 2], [3, 4]], index=['你', '好'])
print(d.index)
print(d.columns)
print(d.values)
print(d[0]['你'])

d = d.reindex(columns=[1, 0], method='ffill', fill_value=0)
print(d.add(pd.DataFrame(np.arange(10).reshape(2, 5)), fill_value=0))
print(d.sort_values(0, ascending=False))
print(d.describe())
print(d.cumsum())
print(d.rolling(2).sum())

print(d.cov())

print('\n# 缺失值 #')
df = pd.DataFrame([[1, 2, 3], [3, 4, np.nan],
                   [12, 23, 43], [55, np.nan, 10],
                   [np.nan, np.nan, np.nan], [np.nan, 1, 2]],
                  columns=['a1', 'a2', 'a3'])
print(df, '\n')
print(df.sample(frac=0.2), '\n')
print('number of nan: ', sum(pd.isnull(df['a1'])))
print(df.dropna(how='all'), '\n')
print(df.dropna(), '\n')
df.fillna(0)
df.fillna(method='ffill')
df.fillna(method='bfill')
df.fillna({'a1': 100, 'a2': 200, 'a3': 300})
