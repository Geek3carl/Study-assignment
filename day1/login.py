#!/usr/bin/env python
import sys
import getpass
afile = 'afile'
bfile = 'bfile'
circulation_num=0  #循环次数初始基数
def deny_account(username):
        print("This account already locked!")
        with open(bfile, 'a+') as bf:     #此处最好为a+模式，本人之前使用a模式错误账号无法写入
            bf.write(username + '\n')
#循环开始
while circulation_num < 3:
    username = input("\033[32;1mPlease input your username:\033[0m")
    flag = False
    with open(afile, 'r') as af:
        for line in af.readlines():
            user, pwd = line.strip().split()
            if username == user:
                password = getpass._raw_input('Please input password:').strip()
                if username == user and password == pwd:
                    print('success!')
                    flag = True
                    break
                else:
                    print('password error,please try again!')
            else:
                if circulation_num < 3:
                    print('User doesn`t exist!')
                    circulation_num += 1
            break
    if flag == True:
        print('Welcome %s come in TG!' % username)
        break
else:
    deny_account(username)