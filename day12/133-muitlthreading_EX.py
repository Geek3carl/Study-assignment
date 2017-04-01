#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/4/1 17:39
# @Author  : Carl
# @Site    : 
# @File    : 133-muitlthreading EX.py
# @Software: PyCharm Community Edition
#
#
#====================Import Modules==================
import threading
import time
#====================================================
def sayhi(num):
    print("running on number:%s"%num)
    time.sleep(3)
if  __name__=='__main__':
    t1=threading.Thread(target=sayhi,args=(1,))
    t2=threading.Thread(target=sayhi,args=(2,))
    t1.start()
    t2.start()
    print(t1.getName())
    print(t2.getName())

#====================================================


