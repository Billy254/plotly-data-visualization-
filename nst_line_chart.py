import pandas as pd
import numpy as np
from plotly.offline import iplot, init_notebook_mode
import plotly.graph_objs as go

pd.set_option('display.max_columns', 10)

df = pd.read_csv('nst-est2017-alldata.csv')

df2 = df[df['DIVISION'] == '1']

df2.set_index('NAME', inplace=True)

# Method 1

cols = []

for col in df2.columns:
    if col.startswith("POP"):
        cols.append(col)

# Using list compression

pop_cols = [col for col in df2.columns if col.startswith('POP')]

pop_df = df2[pop_cols]

data = [go.Scatter(x=pop_df.columns,
                   y=pop_df.loc[name],
                   name=name,
                   mode='lines+markers')
        for name in pop_df.index]

layout = go.Layout(title='Population Growth Comparison',
                   xaxis=dict(title='Years '),
                   yaxis=dict(title='Population'))
fig = go.Figure(data , layout)

iplot(fig)