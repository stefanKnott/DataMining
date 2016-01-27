import sys
import numpy as np
from matplotlib import pyplot as plt

def generateData(attrNum):
	data = getAttrData(attrNum)
	data.sort()
	conclusions = []
	conclusions.append(np.min(data))
	conclusions.append(np.max(data))
	conclusions.append(np.mean(data))
	conclusions.append(np.std(data))
	conclusions.append(np.median(data))
	conclusions.append(np.percentile(data, 25))
	conclusions.append(np.percentile(data, 75))
	conclusions.append(np.percentile(data, 75) - np.percentile(data, 25))
	print "DATA FOR ATTR #:", attrNum
	print "MIN:", np.min(data), ",", "MAX:", np.max(data), ",", "MEAN:", np.mean(data), ",", "STDDEV:", np.std(data), ",", "MEDIAN:", np.median(data), ",", "Q1:",np.percentile(data, 25), ",", "Q3:",np.percentile(data, 75), ",", "IQR: ", np.percentile(data, 75) - np.percentile(data, 25)
	return conclusions

def getAttrData(attrNum):
	data = []
	with open('magic04.data') as dataFile:
		for line in dataFile:
			attributes = line.split(',')[:8]
			attrData = float(attributes[int(attrNum)-1])
			data.append(attrData)
	return data

def generateScatter():
	attr4Data = getAttrData(4)
	attr5Data = getAttrData(5)
	fig = plt.figure()
	ax1 = fig.add_subplot(211)
	ax1.plot(attr4Data, "ro")
	ax1.plot(attr5Data, "bo")
	plt.title('Attribute 4 and 5 Data Points')
	plt.xlabel('ith Data Point')
	plt.ylabel('Attr Measurement')
	plt.legend(['Attribute 4', 'Attribute 5'])
	plt.show()

if __name__ == '__main__':
	generateData(sys.argv[1]) #Generate data of attribute # given via cmd line
	generateScatter() #Generate scatter plot of 4th and 5th attributes

