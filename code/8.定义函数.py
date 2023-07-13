# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 19:19:24 2022

@author: Sigmund
"""
#%%
# 1. 定义函数

# 无参数
def welcome():
    print("欢迎参加我的Python课!")


# 调用函数
#welcome()

#%%
# 1个参数
def welcome(name):
      print(f"{name}, 欢迎参加我的Python课!")

# 调用函数
#welcome('老李')

#%%

# 多个参数
def sum_caculator(x,y,z):
    sum = x+y+z
    print("计算的和:",sum)

# 调用函数
sum_caculator(8,22,38)
sum_caculator(8,22,38,50)

#%%
# 任意参数 *args
def sum_caculator(*args):
    sum = 0
    for n in args:
        sum+=n
    print("计算的和:",sum)

# 调用函数
sum_caculator(8,22)
sum_caculator(8,22,38,50)

#%%
# 任意参数 **kwargs
def info(**kwargs):
    print("Data type of argument:", type(kwargs))
   
    for key, value in kwargs.items():
        print(f"{key}价格为{value}.")

# 调用函数
info(苹果=5.2)
info(苹果=5.2,香蕉=2.2)

#%%

# 默认参数
def sum_caculator(x=8,y,z):
    sum = x+y+z
    print("计算的和:",sum)

# 调用函数
sum_caculator(22,38)

#%%

def sum_caculator(y,z,x=8):
    sum = x+y+z
    print("计算的和:",sum)

# 调用函数
sum_caculator(22,38)

#%%
# 返回值
def sum_caculator(x,y,z):
    sum = x+y+z
    print("计算的和:",sum)
    return sum*y

# 调用函数
sum_caculator(22,38,40)

#%%
# 2. 函数变量

# 局部变量
def subtractor():
    q = 10
    p = 5
    print(q-p)

subtractor()

print(q)

#%%
q = 10

def subtractor():
    global q #调用，已与局部变量区分
    p = 5
    print(q-p)

subtractor()
print(q)

#%%
# 3. 匿名函数


f = lambda x,y,z: x+y+z

f(10,15,30)

#%% 

def f(x,y,z):
    return x+y+z

f(10,15,30)


