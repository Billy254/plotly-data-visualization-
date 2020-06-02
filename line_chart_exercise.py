import pandas as pd
import numpy as np
import plotly.graph_objs as go
from plotly.offline import iplot, init_notebook_mode


def read_data(file):
    return pd.read_csv(file)


file = "2010YumaAZ.csv"
df = read_data(file)


def decribe_data(df):
    print("Sample \n", df.sample(50))
    print("\n Decribe data \n", df.describe())
    print("\n Columns \n", df.columns)
    print("Information", df.info())


data = [go.Scatter(x=df[df['DAY'].str.contains(day)]['LST_TIME'],
                   y=df[df['DAY'] == day]['T_HR_AVG'],
                   mode='lines+markers',
                   name=day)
        for day in df['DAY'].unique()]

layout = go.Layout(title='Daily Temperature line Chart',
                   xaxis={'title': 'X axis'},
                   yaxis={'title': 'y axis'})

fig = go.Figure(data, layout)

iplot(fig)
