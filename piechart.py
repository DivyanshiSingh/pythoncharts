#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 18:27:30 2019

@author: divyanshisingh
"""

import matplotlib.pyplot as plt
slices=[56,34,16,29]
subjects=['python','webdesign','java','coding']
colors=['blue','orange','green','red']
plt.pie(slices, labels=subjects, startangle=90, shadow=True, explode=(0,0,0.1,0),autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()