import pandas as pd
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [1, 6], 'D': [7, 8]})

df = pd.merge(df1, df2, on='A')

print(df)
