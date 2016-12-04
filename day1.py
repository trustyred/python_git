#!/usr/bin/env python
#_*_ coding:utf-8 _*_
admin=raw_input('please input your account: ')
count=3 
f=open('./.tt','r')
for i in f:
    t=i.strip()
    test1=t[:-2] == admin
    test2=t[-1] == '1'
    if test1 and test2:
        print 'your account is locked'
        exit()
while count>0:
    password=raw_input('password is :')
    if password is '123456':
        break
    else:
        print 'password is wrong you have %d times chances ' %(count-1)
    count-=1

if count==0:
    print 'your account is locked'
    f=open('./.tt','aw')
    f.write('%s %d\n' %(admin,1))	#如果第二个字段是0的话则表示没有被锁定如果是1的话则表示被锁定
    f.close()
