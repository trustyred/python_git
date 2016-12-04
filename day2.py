#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#找到重复元素的下标
l=['hello', 'world', 'mo', 'dong', '1', '2', '2', '2', '2', '2', '32', 'dad']
first=0
for i in range(l.count('2')):
	new_list=l[first:]
	aim=new_list.index('2')
	first +=aim+1
	print first
