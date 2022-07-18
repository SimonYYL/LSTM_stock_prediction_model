from ast import increment_lineno
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('https://raw.githubusercontent.com/chendaniely/pandas_for_everyone/master/data/gapminder.tsv',sep='\t')
print(df.head())
print(df.shape)
print(df.columns)
print(df.index)
print(df.values)
print(df.info())
print(df.tail())
# (df.groupby(['year'])[['lifeExp']].mean().reset_index().plot())
# plt.show()
print(df.groupby(['year'])[['lifeExp']].mean().reset_index())
print(df.groupby(['year'])[['lifeExp']].mean().plot())
plt.show()


x = np.arange(0, 5, 0.1)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()