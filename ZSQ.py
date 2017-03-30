#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/30 17:40
# @Author  : Carl
# @Site    : 
# @File    : 装饰器.py
# @Software: PyCharm Community Edition
#理解装饰器
#
import sys


def Before(request, kargs):
    print('before')


def After(request, kargs):
    print('after')


def Filter(before_func, after_func):
    def outer(main_func):
        def wrapper(request, kargs):

            before_result = before_func(request, kargs)
            if (before_result != None):
                return before_result

            main_result = main_func(request, kargs)
            if (main_result != None):
                return main_result

            after_result = after_func(request, kargs)
            if (after_result != None):
                return after_result

        return wrapper

    return outer


@Filter(Before, After)
def Index(request, kargs):
    n=request
    m=kargs
    print('index')
Index(1,2)



