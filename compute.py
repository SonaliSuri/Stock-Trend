from numpy import exp, cos, linspace
import matplotlib.pyplot as plt
import os, time, glob
import plotly as py
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import time as dt_tm
from datetime import date as dt_datepi
import plotly
import plotly.plotly as py
import plotly.tools as plotly_tools
import plotly.graph_objs as go
from plotly.offline import plot
import tempfile
os.environ['MPLCONFIGDIR'] = tempfile.mkdtemp()
from flask import Flask
from flask import render_template
from flask import Markup
from scipy.stats import gaussian_kde
#from IPython.display import HTML
from pandas_datareader import data as datacheck
plotly.tools.set_credentials_file(username='PythonProg',api_key='IHaVOzTpVFFHLXMZVceV')
x = []
y = []
ma = []

def moving_average(interval, window_size):
    window = np.ones(int(window_size))/float(window_size)
    return np.convolve(interval, window, 'same')

def compute(STOCK_NAME='AAPL'):
    quotes = pd.DataFrame(datacheck.DataReader(STOCK_NAME, 'yahoo', '2018-01-01'))
    quotes=quotes.reset_index()
    #quotes.head()
    if len(quotes) == 0:
        print("Couldn't connect to yahoo trading database")
    else:
        dates = quotes['Date']
        y = quotes['Close']
        #print(y)
        for date in dates:
            x.append(date) # Plotly timestamp format
        ma = moving_average(y, 10)
    xy_data = go.Scatter( x=x, y=y, mode='markers', marker=dict(size=4), name=STOCK_NAME )
    # vvv clip first and last points of convolution
    mov_avg = go.Scatter( x=x[5:-4], y=ma[5:-4], \
                    line=dict(width=2,color='green'), name='Moving average' )
    data = [xy_data, mov_avg]
    layout = go.Layout(title='Price', xaxis=dict(title='Months'), yaxis=dict(title='Rolling average'))
    fig = go.Figure(data=data, layout=layout)
    div_output = plot(fig, output_type='div', include_plotlyjs=False)
    return div_output

if __name__ == '__main__':
    print(compute("AAPL"))