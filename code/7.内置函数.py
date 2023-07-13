# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 17:52:35 2022

@author: Sigmund
"""

#%%
# abs(x): 绝对值
a = -5
print(abs(a))

#%%
# min(): 最小值
# max(): 最大值
c = [-2,4,5,-10]
print('最大值:',max(c))
print('最小值:',min(c))

#%%
#round (): 浮点数的四舍五入值
x = 5.456
print(round(x))

y = 5.5555
print(round(y))

#%%
"""
range(): 创建一个整数列表.
range(start, stop, step) 三个参数
   start: 开始数,默认为0
   stop: 结束数，但不包括 stop
   step：步长，默认为1
"""


n = range(100) # 等于range(0:100:1)
print(n) 

m = range(1,100,2) 
print(m) 

print(list(n))
print(list(m))

for i in n:
    print(i)
    

#%%

# input()

fahrenheit = float(input("输入华氏温度: "))

#转换公式
celsius = (fahrenheit - 32) * 5/9

#输出结果
print('%.2f 华氏温度为: %0.2f 摄氏温度' %(fahrenheit, celsius))

#%%


# zip(): 将多个序列（列表、元组、字典、集合、字符串以及range() 区间构成的列表）聚合到一个元组中.

fruits = ['苹果', '香蕉', '桔子','葡萄']
price = [2.59, 0.66, 3.29, 4.45]

fruit_price = zip(fruits, price)

for price in fruit_price:
    print(price)


#%%
# enumerate()

name_list = ['老张', '老王', '老李','老赵']

# 输出序号和名字元组
for name in enumerate(name_list):
    print (name)

# 改变序号，输出序号和名字
for n, name in enumerate(name_list, 100):
    print (n, name)

# 分别输出序号和名字
for n, name in enumerate(name_list):
    print(n)
    print(name)
