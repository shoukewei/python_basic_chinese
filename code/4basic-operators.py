# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 12:30:06 2022

@author: ophel
"""

# 1. 算数运算符

a = 8 
b = 3 

#%%

# 加法
c = a + b
print(c)

#%%

#减法

d = a - b
print(d)

#%%

#乘法
e = a * b
print(e)

#%%

# 除法
f = a / b
print(f)

#%%

#整除，取商
g = a//b
print(g)

#%%

#取模，余数
h = a % b
print(h)

#%%

#幂运算
i = a ** b
print(i)

#%%

#字符串运算

hello = "你好"
name = "世界"
helloworld = hello + " " + name + '!'
print(helloworld)

multihellos = hello * 5
print(multihellos)

#%%

#列表和元组运算
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

fruitList = ['Apple','Banana','Orange']
print(fruitList*2)

#%%

# 3. 比较（关系）运算符
a = 8 
b = 10

print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#%%

# 3. 赋值运算符
a = 5 
a +=1
print(a)

b = 7 
b /= 3
print(b)

#%%

# 4. 逻辑运算符
c = 1
print(c < 2 and c<8)
print(c>2 and c<3)
print(not(c>2 and c<3))


x = 9
print(x<5 or x>8)

print(not(x<0 or x>10))

print(not(x>0 and x<10))
