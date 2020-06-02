import pandas as pd
import numpy as np
from plotly.offline import iplot , init_notebook_mode
import plotly.graph_objs as go

np.random.seed(56)

X_values = np.linspace(0, 1, 100)
y_values = np.random.randn(100)

trace0 = go.Scatter(x=X_values, y=y_values+5, mode='markers', name='markers')

trace1 = go.Scatter(x=X_values, y=y_values, mode='lines', name='lines')

trace2 = go.Scatter(x=X_values, y=y_values-5, mode='lines+markers', name='lines and ,marker')

data =[trace0, trace1, trace2]

layout = go.Layout(title ='Line Chart',
                   xaxis= dict(title ='X axis'),
                   yaxis= dict(title='Y axis'))
fig = go.Figure(data, layout)

iplot(fig,'Line Graph')