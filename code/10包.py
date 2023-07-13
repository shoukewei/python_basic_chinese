# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 21:14:02 2022

@author: Sigmund
"""
#%%

# 方法1
import math

a = math.sin(5)
b = math.sqrt(22299)

print(a)
print(b)

#%%
# 方法2

from math import *

c = sin(5)
d = sqrt(22299)

print(c)
print(d)

#%%

# 方法3
from math import sin, sqrt

e = sin(5)
f = sqrt(22299)

print(e)
print(f)


#%%

# 导入所需包
import pandas as pd
import matplotlib.pyplot as plt

# 导入数据
data = pd.read_csv('./data/water_ph_do.csv')
data.head()

# 查看变量名称
data.columns

# 取出一组数
x = data['ID']
y = data['DO(mg/l)']

# 做图形
plt.plot(x,y)
plt.xlabel('time (hour)',fontsize=15)
plt.ylabel('DO (mg/L)',fontsize=15)
plt.rc('xtick',labelsize=15)
plt.rc('ytick',labelsize=15)
plt.savefig('./results/water_do_signal.png',dpi=300)
plt.show()
