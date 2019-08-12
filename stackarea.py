#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 17:00:48 2019

@author: divyanshisingh
"""

import matplotlib.pyplot as plt
python=[23,34,45,87]
webdesign=[20,54,21,65]
coding=[12,29,37,78]
java=[9,23,15,41]
C=[23,15,35,17]
plt.plot([],[],color='white',label='python',linewidth=5)
plt.plot([],[],color='red',label='webdesign',linewidth=5)
plt.plot([],[],color='green',label='coding',linewidth=5)
plt.plot([],[],color='orange',label='java',linewidth=5)
plt.plot([],[],color='blue',label='C',linewidth=5)
plt.stackplot(python,webdesign,coding,java,C)
colors=['white','red','green','orange','blue']
plt.xlabel('x')
plt.ylabel('y')
plt.title('Stack Plot')
plt.legend()
plt.show()
