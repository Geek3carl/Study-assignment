#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/4/1 19:55
# @Author  : Carl
# @Site    : 
# @File    : 139-multiprocessingEX.py
# @Software: PyCharm Community Edition
# 消息队列
#
#====================Import Modules==================
from multiprocessing import Process
import time
import multiprocessing
#====================================================

def f(q):
    q.put([42,None,'hello'])


if __name__ == '__main__':
    name = multiprocessing.Queue()
    p = Process(target=f, args=(name,))
    p2= Process(target=f,args=(name,))
    p.start()
    p2.start()
    print('from parent:',name.get())
    print('from parent2:', name.get())
    p.join()




