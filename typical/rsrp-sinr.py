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

# m5 = pd.read_csv('014-sinr.csv', delimiter=',', parse_dates=[0], header=None, names=['x', 'd'])
# m14 = pd.read_csv('014-rsrp.csv', delimiter=',', parse_dates=[0], header=None, names=['x', 'd'])

# m5 = pd.read_csv('005-sinr.csv', delimiter=',', parse_dates=[0], header=None, names=['x', 'd'])
# m14 = pd.read_csv('005-rsrp.csv', delimiter=',', parse_dates=[0], header=None, names=['x', 'd'])

m5 = pd.read_csv('sinr_snow.csv', delimiter=',', parse_dates=[0], header=None, names=['x', 'd'])
m14 = pd.read_csv('rsrp_snow.csv', delimiter=',', parse_dates=[0], header=None, names=['x', 'd'])


fig, ax1 = plt.subplots(figsize=(5, 2.5))
ax2 = ax1.twinx()

ax1.plot(m14["x"], m14["d"], label="RSRP")
ax2.plot(m5["x"], m5["d"], label="SINR", color="red", linestyle="dotted")
# ax1.xaxis_date()


for label in ax1.get_xaxis().get_ticklabels():
    label.set_rotation(20)

ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:00'))
ax1.xaxis.set_major_locator(plt.MaxNLocator(6))
ax1.set_xlabel('Time')
ax1.set_ylabel('RSRP (dBm)')
ax2.set_ylabel('SINR (dB)')

lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines = lines + lines2
labels = labels + labels2
fig.legend(lines, labels, bbox_to_anchor=(0.7, 0.5), ncol=2)

plt.tight_layout()

plt.savefig("snow_stats.png", bbox_inches="tight")

# plt.savefig('014-rsrp-sinr.png', dpi='figure', format='png', metadata=None,
#         bbox_inches=None, pad_inches=0.1,
#         facecolor='auto', edgecolor='auto',
#         backend=None
#        )