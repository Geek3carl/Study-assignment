#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/28 14:01
# @Author  : Carl
# @File    : 119-模拟ssh.py
# @Software: PyCharm Community Edition
import socket
import subprocess
ip_port=('127.0.0.1',9999)
sk=socket.socket()
sk.bind(ip_port)
sk.listen(5)
while True:
    print('server waiting...')
    conn,addr=sk.accept()
    while True:
        client_data=conn.recv(1024)
        if not client_data.decode():break
        print("recv cmd:",str(client_data,'utf8'))
        cmd=str(client_data,'utf8').strip()
        cmd_result=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
        conn.send(cmd_result.stdout.read(),'utf8')
    conn.close()
