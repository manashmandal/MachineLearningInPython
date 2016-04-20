__author__ = 'Manash'

import pandas as PD
from pandas import DataFrame
import matplotlib.pyplot as plt
from pylab import *


#file location 
target_url = ("file:\\\E:\ML in python\Chapter2\_abalone.data.txt")

#loading data
abalone = PD.read_csv(target_url, header=None, prefix="V")

abalone.columns = ['Sex', 'Length', 'Diameter', 'Height', 'Whole Weight', 'Sucked Weight', 'Viscera Weight', 'Shell weight', 'Rings']

print abalone.head()
print abalone.tail()

#print summary of dataframe

summary = abalone.describe()

print summary

#box plot the real-valued attributes
#convert to array for plot routine

abalone_array = abalone.iloc[:, 1:9].values

print abalone_array

boxplot(abalone_array)
plt.xlabel("Attribute")
plt.ylabel("Quartile Ranges")
show()

#removing the last column

abalone_array2 = abalone.iloc[:, 1:8].values
boxplot(abalone_array2)
plt.xlabel("Attribute index")
plt.ylabel("Quartile Ranges")
show()

abaloneNormalized = abalone.iloc[:, 1:9]


for i in range(8):
	mean = summary.iloc[1, i]
	sd = summary.iloc[2, i]

	abaloneNormalized.iloc[:, i:(i+1)] = (abaloneNormalized.iloc[:, i:(i+1)] - mean) / sd

abalone_array3 = abaloneNormalized.values

boxplot(abalone_array3)
plt.xlabel("Attribute Index")
plt.ylabel("Quartile Ranges - Normalized")
show()



