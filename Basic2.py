# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 17:09:09 2019

@author: samer
"""
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2 * 3, 400)
y = np.sin(x ** 2)
fig, axs = plt.subplots(2,3,figsize=(10, 5))
axs[0, 0].plot(x, y)
axs[0, 0].set_title('Axis [0, 0]')
axs[0, 1].plot(x*.5, -y, 'tab:red')
axs[0, 1].set_title('Axis [0, 1]')
axs[0, 2].plot(x, 0.3 * y, 'o')
axs[0,2].plot(x, y, '+')
axs[1,0].plot(x, y ,'*')
axs[1,1].plot(x, y*3 ,'tab:red','*')
axs[1,2].plot(x/2, y*3 ,'*')

fig = plt.figure()
ax = plt.axes(projection='3d')
zline = np.linspace(0, 15, 1000)
x = np.sin(zline)
y = np.cos(zline)
ax.plot3D(x, y, zline, 'red')