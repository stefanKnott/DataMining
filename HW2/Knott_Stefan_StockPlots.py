import numpy as np
from matplotlib import pyplot as plt
import datetime as dt
import csv

#col_dtypes = [('ymd', str), ('close', float), ('volume', float), ('open', float), ('high', float), ('low', float)]

fig , axes = plt.subplots(nrows=4, ncols=1, figsize=(12,5))
'''def cdate(x):
    return dt.datetime(int(x[0]), int(x[1]), int(x[2]))
'''
lows, highs, opens, volumes, closes, diffs = [], [], [], [], [], []

with open('HistoricalQuotes(3).csv', 'rb') as f:
	reader = csv.reader(f)
	i = 0
	for row in reader:
		i += 1
		if i == 1:
			continue
		lows.append(row[5])
		highs.append(row[4])
		opens.append(row[3])
		volumes.append(row[2])
		closes.append(row[1])

#Plot daily low and highs
lows.reverse()
highs.reverse()
axes[0].plot(lows, 'r')
axes[0].plot(highs, 'b')


volumes = volumes[1:] #first val is invalid

'''BOX PLOT'''
axes[1].boxplot(np.array(volumes).astype(np.float), vert=True, patch_artist=True)


bins = np.arange(1500000, 2300000, 2100000)


'''Difference between opening and closing values -- AKA daily change'''
for op, close in zip(opens, closes):
	diffs.append(float(close)-float(op))

axes[3].plot(diffs, "r")

plt.show()



