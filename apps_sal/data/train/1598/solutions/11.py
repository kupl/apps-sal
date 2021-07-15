from statistics import mean
from collections import Counter
for _ in range(int(input())):
 n=int(input());d={}
 for i in range(n):
  x,y,z=input().split()
  d[int(z)]=[x,y]
 avg=mean(d);a=[]
 for i in d:
  if(i<avg):a.append(i)
 a.sort();c=0
 for i in range(len(a)-1):
  if(a[i]==a[i+1]):c=1;break
 if(c==1):
  result=sorted(a,key=a.count,reverse=True)
  for i in result:print(*d[i],i)
 else:
  for i in a:print(*d[i],i)
