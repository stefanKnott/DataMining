import numpy as np
from matplotlib import pyplot as plt
import datetime as dt
import csv

#col_dtypes = [('ymd', str), ('close', float), ('volume', float), ('open', float), ('high', float), ('low', float)]
fig , axes = plt.subplots(nrows=2, ncols=1, figsize=(12,5))
'''def cdate(x):
    return dt.datetime(int(x[0]), int(x[1]), int(x[2]))
'''
years = ('2013', '2014', '2015')
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
axes[0].set_title("Daily Highs and Lows Over 3 Years")
axes[0].set_xlabel("Data Point Number")
axes[0].set_ylabel("Price ($)")
#for label in axes[0].get_xticklabels()[1::2]:
 #   label.set_visible(False)
#axes[0].xticks(years)
#axes[0].set_xticklabels(years)
axes[0].legend(loc='best', fontsize=12, shadow=True)


'''BOX PLOT'''
axes[1].set_title("Box Plot of Opens and Closes")
axes[1].set_ylabel("Price $")
axes[1].boxplot(np.array(opens).astype(np.float), vert=True, patch_artist=True)
axes[1].boxplot(np.array(closes).astype(np.float), vert=True, patch_artist=True)


fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12,5))
fvals = [float(i) for i in volumes]
tbins = np.arange(1500000, 23000000, 2100000)
tbins = tbins[:len(tbins)-1]
mu, sigma = np.mean(fvals), np.std(fvals)
x = mu + sigma*np.random.randn(10000)
n, bins, patches = axes[0].hist(x,10, normed=1, facecolor='green', alpha=0.5)
axes[0].set_xticks(bins)
axes[0].set_xlabel("Volume")
axes[0].set_ylabel("Frequency")
axes[0].set_title("Histogram of Volume: mu=" + str(mu) + "sigma="+str(sigma))
axes[0].set_xticklabels(tbins)

#Difference between opening and closing values -- AKA daily change
for op, close in zip(opens, closes):
	diffs.append(float(close)-float(op))
axes[1].set_title("Daily Change (close-open) Over 3 Years")
axes[1].set_xlabel("Data Point Number")
axes[1].set_ylabel("Price Change ($)")
axes[1].plot(diffs, "r")

plt.show()



