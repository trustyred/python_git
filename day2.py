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
	
#方法2
l=['hello', 'world', 'mo', 'dong', '1', '2', '2', '2', '2', '2', '32', 'dad']
first=0
for i in range(l.count('2')):
	if first==0:
		first=l.index('2')
	else :
		first=l.index('2',first+1)
	print first

#高亮搜索的一个例子

staff_data='./staff_data'

f=file(staff_data,'r')
while True:
	info=raw_input("input search info: ")
	for i in f.readlines():
		if info in i.strip():
			page=i.strip().replace(info,'\033[1;32m'+info+'\033[0m')
			print page

	f.seek(0)

