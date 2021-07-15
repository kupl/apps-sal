import numpy
from itertools import permutations 
totals=0
test=int(input())
while(test!=0):
 n=int(input())
 tw=[0,0,0,0]
 th=[0,0,0,0]
 si=[0,0,0,0]
 ni=[0,0,0,0]
 s=[0,1,2,3]
 for i in range(n):
  m,t = map(str,input().split())
  t=int(t)
  if m=="A":
   ind=0
  elif m=="B":
   ind=1
  elif m=="C":
   ind=2
  elif m=="D":
   ind=3
  if t==12:
   tw[ind]+=1
  elif t==3:
   th[ind]+=1
  elif t==6:
   si[ind]+=1
  else:
   ni[ind]+=1
 co = list(permutations(s,4))
 total=float("-inf")
 for value in co:
  p=[tw[value[0]],th[value[1]],si[value[2]],ni[value[3]]]
  p.sort(reverse=True)
  tot=0
  for i in p:
   if i==0:
     tot-=100
  tot+=p[0]*100
  tot+=p[1]*75
  tot+=p[2]*50
  tot+=p[3]*25
  if tot>total:
   total=tot
 print(total)
 totals+=total
 test-=1
print(totals)
