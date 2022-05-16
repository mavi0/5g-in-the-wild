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

m5 = pd.read_csv('rsrp_peaks.csv', delimiter=',', parse_dates=[0], header=None, names=['x', 'rw', 'rm', 'sw', 'sm'])
# m14 = pd.read_csv('rsrp_snow.csv', delimiter=',', parse_dates=[0], header=None, names=['x', 'd'])


fig, ax1 = plt.subplots(figsize=(5, 2.5))
ax2 = ax1.twinx()


ax1.plot(m5["x"], m5["rw"], label="RSRP Representive Site")
ax2.plot(m5["x"], m5["sw"], label="SINR", color="red", linestyle="dotted")
ax1.plot(m5["x"], m5["rm"], label="RSRP Idealised Site")
ax2.plot(m5["x"], m5["sm"], label="SINR", color="red", linestyle="dotted")

# ax1.xaxis_date()


for label in ax1.get_xaxis().get_ticklabels():
    label.set_rotation(20)

ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))
ax1.xaxis.set_major_locator(plt.MaxNLocator(6))
ax1.set_xlabel('Time')
ax1.set_ylabel('RSRP (dBm)')
ax2.set_ylabel('SINR (dB)')

lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines = lines + lines2
labels = labels + labels2
fig.legend(lines, labels, bbox_to_anchor=(0.85, 0.72), ncol=2)

plt.tight_layout()

plt.savefig("rf_peaking.png", bbox_inches="tight")

# plt.savefig('014-rsrp-sinr.png', dpi='figure', format='png', metadata=None,
#         bbox_inches=None, pad_inches=0.1,
#         facecolor='auto', edgecolor='auto',
#         backend=None
#        )










# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
# import pandas as pd
# from scipy.signal import argrelextrema
# from scipy.signal import savgol_filter, find_peaks, find_peaks_cwt
# from pandas import read_csv
# import csv
# import datetime

# df = pd.read_csv('rsrp_peaks.csv', delimiter=',', parse_dates=[0], header=None, names=['x', 'd', 'dd'])

# # df.style.format({"x": lambda t: t.strftime("%Y-%m-%d")}) 

# # df['x'] = df['x'].dt.strftime('%d/%m/%Y %h:%M')

# df.info()

# # ax = df.plot(df['x'], df['d'], label='Download')
# # ax.xaxis.set_major_locator(mdates.DayLocator())

# plt.plot(df['x'], df['d'], label='West Scrafton')
# plt.plot(df['x'], df['dd'], label='Myers Lane')


# #apply a Savitzky-Golay filter
# smooth = savgol_filter(df.d.values, window_length = 351, polyorder = 5)
# smooth2 = savgol_filter(df.dd.values, window_length = 351, polyorder = 5)


# # #find the maximums
# # peaks_idx_max, _ = find_peaks(smooth, prominence = 0.01)

# # #reciprocal, so mins will become max
# # smooth_rec = 1/smooth

# # #find the mins now
# # peaks_idx_mins, _ = find_peaks(smooth_rec, prominence = 0.01)

# plt.xlabel('Time')
# plt.ylabel('Throughput (Mbit/s)')


# plt.plot(df['x'], smooth, label='Smoothed')
# plt.plot(df['x'], smooth2, label='Smoothed')


# #plot them
# # plt.scatter(df.x.values[peaks_idx_max], smooth[peaks_idx_max], s = 55,
# #             c = 'green', label = 'max')
# # plt.scatter(df.x.values[peaks_idx_mins], smooth[peaks_idx_mins], s = 55,
# #             c = 'black', label = 'min')
# plt.legend(loc='center left', ncol=2)

# # plt.locator_params(axis='x', nbins=4)

# # fig, ax = plt.subplots()
# # ax.plot_date(x, y, markerfacecolor='green', markeredgecolor='red', ms=7)
# # fig.autofmt_xdate()
# # ax.set_xlim([datetime.date(2022, 5, 4), datetime.date(2022, 5, 10)])
# # ax.set_ylim([0, 8])

# # every_nth = 100
# # for n, label in enumerate(ax.xaxis.get_ticklabels()):
# #     if n % every_nth != 0:
# #         label.set_visible(False)

# # locations = ['2022-05-04', '2022-05-05', '2022-05-06', '2022-05-07', '2022-05-08', '2022-05-09', '2022-05-10']
# # labels = locations

# # plt.xticks(locations, labels)




# plt.show()
