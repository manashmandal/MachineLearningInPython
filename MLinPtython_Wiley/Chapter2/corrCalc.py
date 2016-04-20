__author__ = 'Manash'

import pandas as PD
from pandas import DataFrame
import matplotlib.pyplot as plot
import sys


#read data 
target_url = ("file:\\\E:\ML in python\Chapter2\sonar.all-data.txt")

#load data
rocksVMines = PD.read_csv(target_url, header =None, prefix = "V-")

#calculate correlation between real valued attributes
dataRow2 = rocksVMines.iloc[1, 0:60]
dataRow3 = rocksVMines.iloc[2, 0:60]
dataRow21 = rocksVMines.iloc[20, 0:60]

mean2 = 0.0
mean3 = 0.0
mean21 = 0.0

numElement = len(dataRow2)

for i in range(numElement):
	mean2 += dataRow2[i] / numElement
	mean3 += dataRow3[i] / numElement
	mean21 += dataRow21[i] / numElement

var2 = 0.0
var3 = 0.0
var21 = 0.0

for i in range(numElement):
	var2 += (dataRow2[i] - mean2) * (dataRow2[i] - mean2) / numElement
	var3 += (dataRow3[i] - mean3)**2 / numElement
	var21 += (dataRow21[i] - mean21)**2 / numElement


corr23 = 0.0
corr221 = 0.0

for i in range(numElement):
	corr23 += ( (dataRow2[i] - mean2) * (dataRow3[i] - mean3) ) / ((var2 * var3)**.5 * numElement)
	corr221 += (( dataRow2[i] - mean2) * (dataRow21[i] - mean21)) / ((var21 * var2)**.5 * numElement)

sys.stdout.write("Correlation between attribute 2 and 3 \n")
print(corr23)
sys.stdout.write(" \n")
sys.stdout.write("Correlation between attribute 2 and 21 \n")
print(corr221)
sys.stdout.write(" \n")