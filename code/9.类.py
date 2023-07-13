# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 18:10:40 2022

@author: Sigmund
"""

#%%
# 1. 创建类
class person():
    pass

#%%

# 创建对象
class person():
    def __init__(name, gender, age, origin, phone):
        pass

#%%

# self 参数
class person():
    def __init__(self, name, gender, age, origin, phone):
        self.name = name
        self.gender = gender
        self.age = age
        self.origin = origin
        self.phone = phone
    

#%%

# 定义更多函数

class person():
    def __init__(self, name, gender, age, origin, phone):
        self.name = name
        self.gender = gender
        self.age = age
        self.origin = origin
        self.phone = phone

    def info_func(self):
         print(f'这是{self.name}, 性别：{self.gender}, 年龄：{self.age}岁。')
         
         if self.gender == '男':
             print(f'他来自{self.origin},他的电话为{self.phone}。')
         else:
             print(f'她来自{self.origin}, 她的电话为{self.phone}。') 

#%%

# 创建实例
person1 = person('小张', '女', 23, '北京', 1525551888)
person2 = person('小李', '男', 21, '山东', 1572221666) 


#%%

# 执行类

# 访问实例的属性
print(person1.name)
print(person2.age)

# 访问实例的方法
person2.info_func() 

#%%

# 2. 类的继承

# 创建子类
class student(person):
    pass

#%%
# 创建子类的实例
student1 = student('小于', '女', 21, '上海', 557889999)
student2 = student('小李', '男', 20, '广东', 657889999)

#%%
# 运行实例
print(student1.phone)
print(student2.phone)

# 访问实例的方法
student1.info_func()

