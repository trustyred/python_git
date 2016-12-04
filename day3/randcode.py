#!/usr/bin/env python
#coding:utf-8

import random

code=list()

for i in range(6):
	if i == random.randrange(0,6):
		code.append(str(random.randrange(0,10)))
	else :
		code.append(chr(random.randrange(65,91)))
print code
s=''.join(code)
print s
