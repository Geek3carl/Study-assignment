#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/28 14:01
# @Author  : Carl
# @Site    : 
# @File    : 119-模拟ssh-client.py
# @Software: PyCharm Community Edition
import socket
ip_port=('127.0.0.1',9999)
sk=socket.socket()
sk.connect(ip_port)
while True:
    user_input=input("cmd:").strip()
    if len(user_input)==0:continue
    if user_input=='q':break
    sk.send(bytes(user_input,encoding='utf8'))
    server_reply=sk.recv(1024)
    print(str(server_reply,'utf8'))
sk.close()
