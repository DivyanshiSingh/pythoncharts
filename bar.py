#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 16:42:39 2019

@author: divyanshisingh
"""

import matplotlib.pyplot as plt
x=[12,32,34,39,67]
y=[34,11,45,68,27]
plt.bar(x,y,label="Growth 1",color="blue")
x1=[34,45,56,19,69]
y1=[54,67,89,45,78] 
plt.bar(x1,y1,label="Growth 2",color="orange")
plt.legend()
plt.xlabel("number")
plt.ylabel("height")
plt.title("Information")
plt.show()