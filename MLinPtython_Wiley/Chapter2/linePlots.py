__author__ = 'Manash'

import pandas as PD
from pandas import DataFrame
import matplotlib.pyplot as plot



#read data 
target_url = ("file:\\\E:\ML in python\Chapter2\sonar.all-data.txt")

#load data
rocksVMines = PD.read_csv(target_url, header =None, prefix = "V-")

for i in range(208):
	#assign color based on "M" or "R" labels
	if rocksVMines.iat[i, 60] == "M":
		pcolor = "red"
	else:
		pcolor = "blue"

	#plot rows of data as if they were series data
	dataRow = rocksVMines.iloc[i, 0:60]
	dataRow.plot(color = pcolor)

	print dataRow

plot.xlabel("Attribute index")
plot.ylabel("Attribute Values")
plot.show()