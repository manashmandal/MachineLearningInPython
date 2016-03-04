# -*- coding: utf-8 -*-
"""
Created on Fri Mar 04 04:13:05 2016

@author: Manash
"""

#import neurolab as nl
#import numpy as np
#
## Create train samples
#x = np.linspace(-7, 7, 20)
#y = np.sin(x) * 0.5
#
#size = len(x)
#
#inp = x.reshape(size,1)
#tar = y.reshape(size,1)
#
#
#
## Create network with 2 layers and random initialized
#net = nl.net.newff([[-7, 7]],[5, 1])
#
## Train network
#error = net.train(inp, tar, epochs=500, show=100, goal=0.02)
#
## Simulate network
#out = net.sim(inp)
#
#print net
#
## Plot result
#import pylab as pl
#pl.subplot(211)
#pl.plot(error)
#pl.xlabel('Epoch number')
#pl.ylabel('error (default SSE)')
#
#x2 = np.linspace(-6.0,6.0,150)
#y2 = net.sim(x2.reshape(x2.size,1)).reshape(x2.size)
#
#y3 = out.reshape(size)
#
#pl.subplot(212)
#pl.plot(x2, y2, '-',x , y, '.', x, y3, 'p')
#pl.legend(['train target', 'net output'])
#pl.show()


#import neurolab as nl
#
#input = np.random.uniform(0, 0.1, (1000, 225))
#output = input[:,:10] + input[:,10:20]
## 2 layers with 225 inputs 50 neurons in hidden\input layer and 10 in output
## for 3 layers use some thet: nl.net.newff([[0, .1]]*225, [50, 40, 10])
#net = nl.net.newff([[0, .1]]*225, [50, 10])
#net.trainf = nl.train.train_bfgs
#
#e = net.train(input, output, show=1, epochs=100, goal=0.0001)

import neurolab as nl

# Logical &
input = [[0, 0], [0, 1], [1, 0], [1, 1]]
target = [[0], [1], [1], [0]]

# Create net with 2 inputs and 1 neuron
net = nl.net.newff([[0, 1],[0, 1]], [3, 1])

# train with delta rule
# see net.trainf
error = net.train(input, target, epochs=100000)

# Plot results
import pylab as pl
pl.plot(error)
pl.xlabel('Epoch number')
pl.ylabel('Train error')
pl.grid()
pl.show()
