import math

for i in range(int(input())):
 y=int(input())
 x=list(map(int,input().split()))
 pr=1
 for j in x:
  pr=pr*j
 #s=min(x)
 m=max(x)
 #m=int(math.sqrt(m))
 #s=int(math.sqrt(s))
 rm=1
 #print s,m
 for k in range(2,m):
  #print k
  if pr%k**2==0:
   rm=k
   break
 print(rm) 
 

