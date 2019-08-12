#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 16:52:47 2019

@author: divyanshisingh
"""

import matplotlib.pyplot as plt
x=[1.2,3.4,5,6,4.7]
y=[5.6,3.4,7.6,2,4.9]
plt.scatter(x,y,label="scat",color="red")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Chart")
plt.legend()
plt.show()