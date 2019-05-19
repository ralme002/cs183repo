#!/usr/bin/env python3

pfr=0
aq=0

p='p'
pcount=0
a='a'
acount=0
h= 'maillog'
g= 'hourlyInfo'
oldctime='0';

newfile=open(g,'w')

with open(h) as fp:
   line = fp.readline()
   while line:
     current = line[21]
     ctime = line[11]
     cctime= line[10]
     if current == p:
      pcount+=1
     elif current == a:
      acount+=1 
 
     if ctime != oldctime:
      oldctime=ctime
      newfile.write(line[:12]+ " postfix rejects:" + str(pcount) + "]   [amavis quarantine:" + str(acount)+ "]"+ '\n') 
     line = fp.readline()   

newfile.close()
