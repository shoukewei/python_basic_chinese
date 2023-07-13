# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 11:09:43 2022

@author: ophel
"""

#%%
# 整数
age = 25
print(age)
#%%
# 浮点
height = 175.5
print(height)

# 复数
z = 3 + 5j
print(z)
#%%
# 字符串
name = '老李'
print(name)

# 长字符串，用三个双引号，或者单引号
triple_string1 = """非常长的句子..."""
triple_string2 = '''非常长的句子...'''

print(triple_string1)
print(triple_string2)
#%%
#多行
"""
作者: 魏守科
日期: 2022年10月2日
此代码是......
"""
print("您好！")

#%%
#布尔类型
A = 20
B = 30
print(A>B)
print(A<B)

#%%

#多数据赋值
x, y, z = 30, 85.5, '苹果'
print(x)
print(y)
print(z)

#%%
#列表
fruitList = ['苹果','香蕉','桔子', '葡萄']
print(fruitList)

#数组
fruitTuple = ('苹果','香蕉','桔子', '葡萄')
print(fruitTuple)

#字典
fruitDict = {
'名称': '苹果',
'颜色': '红色',
'甜': True,
'价格': 2.0}
print(fruitDict)

#%%
# 输出数据类型
a = "这是一个商店。"
b = ['苹果','香蕉','桔子', '葡萄']
c =  {
'名称': '苹果',
'颜色': '红色',
'甜': True,
'价格': 2.0}

print(type(a))
print(type(b))
print(type(c))

#%%
# 输出数据长度
a = "这是一个商店。"
b = ['苹果','香蕉','桔子', '葡萄']
c =  {
'名称': '苹果',
'颜色': '红色',
'甜': True,
'价格': 2.0}

print(len(a))
print(len(b))
print(len(c))

#%%
# 访问列表和元组数据元素

b = ['苹果','香蕉','桔子', '葡萄']

print(b[0])
print(b[-1])
print(b[2:3])
print(b[:3])

#%%

#访问字典元素
fruitDic =  {
'名称': '苹果',
'颜色': '红色',
'甜': True,
'价格': 2.0}

print(fruitDic['价格'])

# get() 法
x = fruitDic.get('名称')
print(x)

# keys()方法获得字典所有键
keys = fruitDic.keys()
print(keys)

# values()获得字典所有值
values = fruitDic.values()
print(values)

#%%
# 数据类型转换
a = 5
b = float(5)
c = str(a)

print(a)
print(b)
print(c)

d = int(b)
e = int(c)
print(d)
print(e)

fruitTuple = ('苹果','香蕉','桔子', '葡萄')
fruitList = list(fruitTuple)
print(fruitList)

fruitTuple1 = tuple(fruitList)
print(fruitTuple)

fruit_list = ['苹果','香蕉','桔子', '葡萄']
fruit_price = [5.7, 2.5,3.8,6.0]
fruit_dict = dict(zip(fruit_list,fruit_price))
print(fruit_dict)


#%%