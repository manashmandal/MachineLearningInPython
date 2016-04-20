__author__ = 'Manash'

import pandas as PD
from pandas import DataFrame
import matplotlib.pyplot as plot



#read data 
target_url = ("file:\\\E:\ML in python\Chapter2\sonar.all-data.txt")

#load data
rocksVMines = PD.read_csv(target_url, header =None, prefix = "V-")

#print summary of data frame
summary = rocksVMines.describe()

print summary

# head of the data
print rocksVMines.head()

#tail of the data
print rocksVMines.tail()

