__author__ = 'Manash'

import pandas as PD
from pandas import DataFrame
import matplotlib.pyplot as plot
from random import uniform


#read data 
target_url = ("file:\\\E:\ML in python\Chapter2\sonar.all-data.txt")

#load data
rocksVMines = PD.read_csv(target_url, header =None, prefix = "V-")


#Change the targets to numeric values
target = []

for i in range(208):
	#assign 0 or 1 target value based on "M" or "R" labels

	if rocksVMines.iat[i, 60] == "M":
		target.append(1.0)
	else:
		target.append(0.0)


#Plot the 35th attribute

dataRow = rocksVMines.iloc[0:208, 35]
plot.scatter(dataRow, target)

plot.xlabel("Attribute Value")
plot.ylabel("Target Value")
plot.show()

#To imporve the visualization, this version dithers the point a little

target = []

for i in range(208):
	if rocksVMines.iat[i, 60] == "M":
		target.append(1.0 + uniform(-0.1, 0.1))
	else:
		target.append(0.0 + uniform(-0.1, 0.1))


dataRow = rocksVMines.iloc[0:208, 35]

plot.scatter(dataRow, target, alpha=0.5, s=120)
plot.xlabel("Attribute Values")
plot.ylabel("Target Values")
plot.show()
