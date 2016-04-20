__author__ = 'Manash'

import pandas as PD
from pandas import DataFrame
import matplotlib.pyplot as plot



#read data 
target_url = ("file:\\\E:\ML in python\Chapter2\sonar.all-data.txt")

#load data
rocksVMines = PD.read_csv(target_url, header =None, prefix = "V-")

dataRow2 = rocksVMines.iloc[1, 0:60]
dataRow3 = rocksVMines.iloc[2, 0:60]

#plotting the data
plot.scatter(dataRow2, dataRow3)

plot.xlabel("2nd Attribute")
plot.ylabel(("3rd Attribute"))
plot.show()

dataRow21 = rocksVMines.iloc[20, 0:60]
plot.scatter(dataRow2, dataRow21)

plot.xlabel("2nd Attribute")
plot.ylabel("21st Attribute")
plot.show()

