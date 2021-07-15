from math import *
for u in range(int(input())):
 n,k=list(map(int,input().split()))
 l=list(map(int,input().split()))
 x,y=1,max(l)
 while(x!=y):
  m=(x+y)//2
  s=0
  for i in l:
   s+=ceil(i/m)
  if(s<=k):
   y=m
  else:
   x=m+1
 print(x)

