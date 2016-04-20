import numpy
from sklearn import datasets, linear_model
from math import sqrt
import matplotlib.pyplot as plt

def xattrSelect(x, idxSet):
	#takes Xmatrix as list of list and returns subset containing columns in idxSet
	xOut = []
	for row in X:
		xOut.append([row[i] 