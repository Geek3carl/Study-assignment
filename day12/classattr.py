#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/28 17:45
# @Author  : Carl
# @Site    : 
# @File    : 114面向对象特性之多态.py
# @Software: PyCharm Community Edition


# class Foo:
#
#     def __init__(self, name):
#         self.name = name
#
#     def ord_func(self):
#         """ 定义普通方法，至少有一个self参数 """
#
#         # print self.name
#         print('普通方法')
#
#     @classmethod
#     def class_func(cls):
#         """ 定义类方法，至少有一个cls参数 """
#
#         print('类方法')
#
#     @staticmethod
#     def static_func():
#         """ 定义静态方法 ，无默认参数"""
#
#         print('静态方法')
#
# # 调用普通方法
# f = Foo()
# f.ord_func()
#
# # 调用类方法
# Foo.class_func()
#
# # 调用静态方法
# Foo.static_func()
#
# # ############### 定义 ###############
# class Foo:
#
#     def func(self):
#         pass
#
#     # 定义属性
#     @property
#     def prop(self):
#         print("prop")
#         pass
# # ############### 调用 ###############
# foo_obj = Foo()
#
# foo_obj.func()
# foo_obj.prop   #调用属性

class Goods(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        print(new_price)
        return new_price

    @price.setter
    def price(self,value):
        self.original_price = value
        print()

    @price.deleter
    def price(self):
        del self.original_price
        print()

obj = Goods()
obj.price         # 获取商品价格
obj.price = 200   # 修改商品原价
del obj.price     # 删除商品原价
