

import sys


t=int(int(sys.stdin.readline().rstrip()))
while t:
 t=t-1
 
 a,b=list(map(int,sys.stdin.readline().rstrip().split(' ')))
 li=[]
 lir=[]
 lic=[]
 for i in range(0,a):
   li.append(sys.stdin.readline().rstrip())
   if '*' in li[i]:
    lir.append(i)
    lic.append(li[i].find('*'))
    lic.append(li[i].rfind('*'))
 
 if not lir:
  print(0)
 else:
  

  r=int(int(max(lir))+int(min(lir)))/2
  c=int(int(max(lic))+int(min(lic)))/2

  ans=int(max((max(lir)-r),(max(lic)-c),(r-min(lir)),(c-min(lic))))

  print(ans+1)

