#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/30 16:57
# @Author  : Carl
# @Site    : 
# @File    : 130-异常处理.py
# @Software: PyCharm Community Edition
#
#
# ====================Import Modules====================
import sys



#=======================================================
#Error type
# SyntaxError 语法错误
# IndentationError
# UnboundLocalError未设置的变量
# EOFError
# AssertionErrot断言错误,条件判断
# zeroDivisionError 0除错误
#
# ======================================================
# 自定义错误类型
class NetError(Exception):
    pass

class HostError(Exception):
    pass

class TimeoutError(Exception):
    pass

class ProtocolError(Exception):
    pass

while   True:
    try:
        num1 = input('num1:')
        num2 = input('num2:')
    except EOFError as e:
        print("User interrupt!")
    except KeyboardInterrupt as e:
        print("User intterupt!")
    try:
        num1=int(num1)
        num2=int(num2)
        result=num1+num2
    except ValueError as e:
        print("Input date type Error!",e)
    except IndentationError as e:
        print("Indent Error!")
    except IndexError as e:
        print("Index Error:",e)
    except EOFError as e:
        print("User interrupt!")
    except KeyboardInterrupt as e:
        print("User intterupt!")
    except Exception as e:
        print("Unknow error type!",e)
    finally:
        print("no matter right or wrong,run this anyway!")










