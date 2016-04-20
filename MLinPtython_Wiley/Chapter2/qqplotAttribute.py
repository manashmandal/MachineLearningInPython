__author__ = 'Manash'

import urllib2
import sys
import numpy as NP
import pylab
import scipy.stats as stats

#read data 
target_url = ("file:\\\E:\ML in python\Chapter2\sonar.all-data.txt")

#load data
data = urllib2.urlopen(target_url)


#arrange data into list ofr labels

xList = []
labels = []

for line in data:
	#split on comma
	row = line.strip().split(",")
	xList.append(row)

nrow = len(xList)
ncol = len(xList[1])

type = [0] * 3

colCounts = []

#generate summary stats for col 3

col = 3
colData = []

for row in xList:
	colData.append(float(row[col]))

colNPArray = NP.array(colData)
sortedArray = NP.sort(colNPArray)

print sortedArray

stats.probplot(colData, dist="norm", plot=pylab)
pylab.show()