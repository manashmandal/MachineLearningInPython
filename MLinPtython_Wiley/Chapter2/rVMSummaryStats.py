__author__ = 'Manash'

import urllib2
import sys
import numpy as NP

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

colArray = NP.array(colData)

colMean = NP.mean(colArray)
colStandardDeviation = NP.std(colArray)

sys.stdout.write("Mean = " + '\t' + str(colMean) + '\t\t' + "Standard Deviation = " + '\t' + str(colStandardDeviation) + "\n")

#calculate quantile boundary
ntiles = 4

percentBoundary = []

for i in range(ntiles + 1):
	percentBoundary.append(NP.percentile(colArray, i * (100) / ntiles))

sys.stdout.write("\nBoundaries for 4 equal percentiles \n")
print(percentBoundary)

sys.stdout.write(" \n")

# run with 10 equal intervals

ntiles = 10

percentBoundary = []

for i in range(ntiles + 1):
	percentBoundary.append(NP.percentile(colArray, i * (100) / ntiles))

sys.stdout.write("Boundaries for 10 Equal Percentiels \n")
print(percentBoundary)
sys.stdout.write(" \n")

# The last column contains categorial variables

col = 60
colData = []

for row in xList:
	colData.append(row[col])


unique = set(colData)
sys.stdout.write("Unique label values \n")
print(unique)

#count up the number of elements having each value
catDict = dict(zip(list(unique) ,range(len(unique))))

catCount = [0] * 2

print catDict

for elt in colData:
	catCount[catDict[elt]] += 1


sys.stdout.write("\nCounts for Each Value of categorial label \n")
print(list(unique))
print(catCount)