# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt


file='test0.txt'

data = np.loadtxt(file, skiprows=9)

plt.figure()

t=data[:,5]
a=data[:,0]

