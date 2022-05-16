import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib as mpl
import pandas as pd
from scipy.signal import argrelextrema
from scipy.signal import savgol_filter, find_peaks, find_peaks_cwt
from pandas import read_csv
import csv
import datetime



m5 = pd.read_csv('014-sinr.csv', delimiter=',', parse_dates=[0], header=None, names=['x', 'd'])
m14 = pd.read_csv('014-rsrp.csv', delimiter=',', parse_dates=[0], header=None, names=['x', 'd'])

# m5 = pd.read_csv('005-sinr.csv', delimiter=',', parse_dates=[0], header=None, names=['x', 'd'])
# m14 = pd.read_csv('005-rsrp.csv', delimiter=',', parse_dates=[0], header=None, names=['x', 'd'])


mpl.rcParams['figure.figsize'] = 5, 2.5

# smooth = savgol_filter(m5.d.values, window_length = 351, polyorder = 5)
# smooth2 = savgol_filter(m14.d.values, window_length = 351, polyorder = 5)

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()

# # the ax keyword sets the axis that the data frame plots to
m14.plot(ax=ax1, x='x', y='d', legend=False, label='RSRP')
m5.plot(ax=ax2, x='x', y='d', legend=False, label='SINR', color='r', linestyle='dotted')

ax1.xaxis_date()
for tick in ax1.get_xticklabels():
    tick.set_rotation(20)

myFmt = mdates.DateFormatter('%Y-%M-%d')
ax1.xaxis.set_major_formatter(myFmt)
ax1.set_xlabel('Time')
ax1.set_ylabel('RSRP (dBm)')
ax2.set_ylabel('SINR (dB)')
ax1.legend(loc='upper left')
ax2.legend(loc='lower right')



plt.tight_layout()


plt.savefig('014-rsrp-sinr.png', dpi='figure', format='png', metadata=None,
        bbox_inches=None, pad_inches=0.1,
        facecolor='auto', edgecolor='auto',
        backend=None
       )