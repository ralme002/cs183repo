#!/usr/bin/python

import sys

#print '#', len(sys.argv), 'arguments.'
#print 'list: ', str(sys.argv)

x = len(sys.argv)
y = str(sys.argv)

#print x

count = 1
while (count < x):
	#print(str(sys.argv[count]))
	f = open(str(sys.argv[count]),"r")
 	print(f.read())
	count = count + 1



