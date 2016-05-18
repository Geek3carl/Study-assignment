#!/usr/bin/env python
import sys
import os
import getpass
import collections
商品={
    '图书':{
        "《Puppet实战》":39,
        "《ZooKeeper分布式过程协同技术详解》":48,
        "《代码审计》":42,
        "《白帽子讲浏览器安全》":73,
    },
    '数码家电':{
        "Iphone6S":6000,
        "MacBookAir":15000,
        "DELL-R720":33000,
        "索尼PlayStation VR":2600,},
    '食品':{
        "茉莉花茶":3,
        "康师傅红烧牛肉面":3,
        "3+2饼干":5.5,
        "红牛":7,
    },
    '生活用品':{
      "汰渍洗衣液-550ml":23,
      "清风抽纸:300抽/三层":12,
      "电神水壶":98,
      "六神花露水":19,
    }
}
#定义各项初始值
money='account.txt'
logtime=0
afile='afile.txt'
bfile='bfile.txt'
SHOPING=[]

#显示余额
def show_money():
    with open(money,'r+') as ac:
        for line in ac.readlines():
            yue = line.strip()
            return int(yue)

def deny_account(username):
    print("This account already locked!")
    with open(bfile,'a+') as bf:  # 此处最好为a+模式，本人之前使用a模式错误账号无法写入
        bf.write(username + '\n')
#程序开始
flag=False
while logtime < 3:
    username = input('\033[31;1m请输入用户名:\033[0m')
    with open(bfile, 'r') as lock_f:
        # 取出黑名单中的用户名与输入的用户名进行匹配
        for line in lock_f.readlines():
            if len(line) == 0:
                continue
            if username == line.strip():
                sys.exit('\033[32;1m用户 %s 已经被锁定!\033[0m' % username)
    # 如果用户名为空重新输入
        if len(username) == 0:
            print('用户名不能为空，请重新输入')
            continue
    with open(afile,'r') as af:
        for line in af.readlines():
            user,pwd = line.strip().split()
            if username == user:
                password = getpass._raw_input('请输入用户%s的密码:'%username).strip()
                if username == user and password == pwd:
                    print('登陆成功！')
                    flag=True
                    break
                else:
                    if logtime<3:
                        print('密码错误请重新输入!')
                    logtime+=1
                    break
        else:
            if logtime<3:
                print('用户不存在!')
            logtime += 1
    if flag==True:
        print('Welcome %s come in TG!' % username)
        break
else:
    deny_account(username)
if flag==True:
    while True:
        if show_money() < 0:
            name1 = "\033[1;31;1m您的账户余额不足，请尽快充值！"
            print(name1.center(50, '-'))
        else:
            print('*'*50)
            欢迎信息 = '\033[1;31;1m欢迎登录没有小菊花的网上超市！\033[0m'
            print(欢迎信息.center(54, '*'))
            yue2='您的账户余额为%s¥元' % show_money()
            print(yue2.center(50,'*'))
            print('\033[1;32;1m*\033[1m' * 50)
            for lei in 商品:
                print('\033[1;35;1m%s\033[1m'%lei)
               # print('\033[1;35;1m%s\033[1m'%lei)
                print('\033[1;32;1m*\033[1m'*50)
                选择类 = input('\033[1;34;1m请选择类目：\033[0m')
        #二级流程
                for s,v in 商品[选择类].items():
                    print('\033[1;32;1m-\033[1m' * 50)
                    print('\033[1;35;1m%s：单价%s¥\033[1m'%(s,v))
                    print('\033[1;32;1m-\033[1m' * 50)
                    选择商品=input('请选择商品:')
                    n = input('输入数量:')
                    jiage=商品[选择类][选择商品]
                    print('\033[1;31;1m本商品单价为:%d¥，本次共计添加%d个,总价为%d*%d=%d¥\033[0m'%(jiage,int(n),jiage,int(n),jiage*int(n)))
                    SHOPING.extend([jiage*int(n)])
                    print('\033[1;32;1m-\033[1m' * 50)
                    xuanze=input('\033[1;31;1m是否继续购物，Y键返回主菜单，N进入购物车结算，请选择！\033[0m')
            #进入购物车结算
                    if xuanze =='N':
                        print('%s'%SHOPING)
                        结算=input('是否结算？Y/N')
                        if 结算 =='Y':
                            余额=show_money()-int(sum(SHOPING))
                            print(余额)
                            with open(money, 'w+') as ac:
                                ac.writelines('%s'%余额)    #计算余额，保存到文件
                        继续=input('是否继续购物(Y/N)?退出:N,返回上一级:Y.')
                        if 继续=='Y':
                            sys.exc_traceback()
                        else:
                            sys.exit()
                    elif xuanze=='Y':
                        break
                else:
                    print("您选择的商品不存在！请重新选择！")
                    break
            else:
                print("选择的类目不存在！")
                continue
            break
        break
