# -*- coding: utf-8 -*-
"""data_cleaning.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1q7GObSstlI30x4RRqhMfdwUQRyvG5iRb
"""

import pandas as pd
df=pd.read_csv("stock .csv",skiprows=2)

df.head()

df['Date']=pd.to_datetime(df['Date'],dayfirst=True)

df.set_index("Date",inplace=True)

print(df.head())

df.columns=['Close','High','Low','Open','Volume']

print(df.head())

df.describe()

print(df.dtypes)

#categorical dat to check if present convert into numerical form
non_numeric=df.select_dtypes(exclude=['number','datetime'])

print(non_numeric.head())

for col in non_numeric:
  print(f"\nUnique values in {col}:")
  print(df[col].unique())