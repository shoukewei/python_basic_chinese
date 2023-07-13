# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 15:51:56 2022

@author: ophel
"""

# 1. 条件控制语句

# if 如果

age = 65

if age >= 60:
    print('属老年人')

#%%

# if-else 如果...除此

n = 35

if n%2 == 0:
    print('此数为偶数')
else:
    print('此数为奇数')

#%%

# if-elif-else语句,如果...如果...除此...

saleFruit = ['苹果', '桔子', '西瓜', '葡萄']
stockFruit = ['苹果', '桔子', '西瓜', '葡萄']

if '香蕉' in saleFruit:
    print('香蕉正在出售.')
elif '香蕉' in stockFruit:
    print('香蕉在库中。')
else:
    print('香蕉缺货!')
    
    
#%%

# 2. while循环语句

# while语句:当...时
num = 10

while num > 0:
    num -= 1  # num = num -1
    print(num)
    
#%%
# while-else语句:当...时,除此...
num = 10

while num > 3:
    num -= 1  # num = num -1
    print(num)
else:
    print('数字不再大约3。')
    
#%%

# while-if-elif-else语句

number = 15

while num != 15:
    num = int(input('猜猜看!请输入一个数字 :  '))
    if num == 15:
        print('厉害! 猜对了！')
    else:
        print('不对！再猜！')

#%%

# 3. for循环语句
# for语句:对于...
fruitList = ['苹果', '桔子', '西瓜', '葡萄']

for items in fruitList:
    print(items)

#%%

# for-if-else语句
fruitList = ['苹果', '桔子', '西瓜', '葡萄']

for items in fruitList:
    if items == '西瓜':
        print('有西瓜在卖。')
        break
    else:
        print("正在查找西瓜。")

#%%
# for-for语句
    
attributeList = ['红', '大','甜']
fruitList = ['苹果', '桔子', '西瓜']

for x in attributeList:
    for y in fruitList:
        print(x, y)


#%%
# 4. 跳转语句

# break
num = 10

while num > 0:
    num -= 1  # num = num -1
    print(num)
    
    if num==5:
        break
    
#%%
num = 10

while num > 0:
    num -= 1  # num = num -1
    print(num)
    
    if num==5:
        continue
    
#%%

num = 10

while num > 0:
    num -= 1  # num = num -1
    
    
    if num==5:
        continue
    print(num)