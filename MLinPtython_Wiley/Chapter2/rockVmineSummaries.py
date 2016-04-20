__author__ = 'Manash'

import urllib2
import sys

#read data from uci data repo
#target_url = ("http://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

#loading local file
target_url = ("file:\\\E:\ML in python\Chapter2\sonar.all-data.txt")

data = urllib2.urlopen(target_url)

#arrange data into list for labels and list of lists for attributes
xList = []
labels = []
for line in data:
	#split on comma
	row = line.strip().split(",")
	xList.append(row)

sys.stdout.write("Number of Rows of Data = " + str(len(xList)) + '\n')
sys.stdout.write("Number of Columns of Data = " + str(len(xList[1])))

