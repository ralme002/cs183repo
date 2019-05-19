#!/usr/bin/env python3
import sys
import re
import array
import os
from itertools import groupby

inputf= 'maillog'
outputf='connect'
lookfor= 'log2'
newfile=open(outputf,'w')
unkfile=open('unknown','w')
knofile=open('known','w')

with open(inputf) as fp:
   line = fp.readline()
   while line:
     x=re.search(r'\b(connect from)\b',line)  
     if x:
       newfile.write(line[42:])
     line = fp.readline()     
   newfile.close()

with open(outputf) as bp:
   line = bp.readline()
   while line:
    x=re.search(r'\b(unknown)\b',line)
    if x:
     unkfile.write(line[20:])
    else:
     knofile.write(line[25:])
    line = bp.readline()

unkfile.close()
knofile.close() 

maxip=0
maxcount=0
count=0
currentip=0

with open('unknown') as xp:
    line = xp.read()
    ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}',line)
    myList= [0]*len(ip)
    for i in ip:
       myList.append(i)
    for x in myList:
     currentip=x
     count=0
     for i in ip:
         if i == x:
          count+=1
     if count > maxcount:
         maxcount=count
         maxip=currentip
   # print (maxcount)
   # print (maxip)   

max2count=0
max2ip=0

with open('known') as hp:
    line2 = hp.read()
    hp = re.findall(r'[0-9]+(?:\.[0-9]+){3}',line2)
    myList2=[0]*len(hp) 
    for n in hp:
      myList2.append(n)
    for j in myList2:
      curren2tip=j
      count2=0
      for k in hp:
        if j == k:
         count2 +=1

      if count2 > max2count:
       max2count=count2
       max2ip=curren2tip

f=open(lookfor, "w")              
f.write("Total Known connection: " + str(len(hp)) +" - [" + str(max2ip) + "] accounts for "+str(max2count)+" connections \n")

f.close()
g=open(lookfor, "a")
g.write("Total Unknown connections: "+str(len(ip))+" - ["+str(maxip)+"] accounts for " +str(maxcount)+" connections \n")
g.close

os.remove("unknown")
os.remove("known")
os.remove("connect")
