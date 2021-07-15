from bisect import insort
from math import ceil
for _ in range(int(input())):
 n,k=map(int,input().split( ))
 array=list(map(int,input().split( )))
 ans=0
 for i in range(n):
  count=[0]*(2001)
  temp=[]
  for j in range(i,n):
   count[array[j]]+=1
   insort(temp,array[j])
   m=ceil(k/(j-i+1))
   t=ceil(k/m)
   x=temp[t-1]
   f=count[x]
   if count[f]:
    ans+=1
 print(ans)
