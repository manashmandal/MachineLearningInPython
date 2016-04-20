__author__ = 'Manash'

import pandas as PD
from pandas import DataFrame
import matplotlib.pyplot as plot



#read data 
target_url = ("file:\\\E:\ML in python\Chapter2\sonar.all-data.txt")

#load data
rocksVMines = PD.read_csv(target_url, header =None, prefix = "V-")

#calculate correlation between real-valued attributes
corrMat = DataFrame(rocksVMines.corr())

#Visualize correlations using heatmap
plot.pcolor(corrMat)
plot.show()