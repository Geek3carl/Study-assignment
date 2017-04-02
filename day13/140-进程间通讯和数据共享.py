#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/4/2 17:31
# @Author  : Carl
# @Site    : 
# @File    : 140-进程间通讯和数据共享.py
# @Software: PyCharm Community Edition
# 管道
#
#====================Import Modules==================
import sys

#====================================================
from multiprocessing import Process, Pipe,Manager
#
#
# def f(conn):
#     conn.send([42, None, 'hello'])
#     conn.close()
#
#
# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()
#     p = Process(target=f, args=(child_conn,))
#     p.start()
#     print(parent_conn.recv())  # prints "[42, None, 'hello']"
#     p.join()



def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.append(1)
    print(l)


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()

        l = manager.list(range(5))
        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, l))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()

        print(d)
        print(l)


