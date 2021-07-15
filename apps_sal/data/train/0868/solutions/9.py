from math import ceil
from bisect import insort
for z in range(int(input())):
 n,k=list(map(int,input().split()))
 a=list(map(int,input().split()))
 c=0
 i=0
 pos=[]
 while i<n:
  pos.append(ceil(k/(ceil(k/(i+1)))))
  i+=1
 i=0
 while i<n-1:
  h=[]
  cl=[0]*2001
  j=0
  while i+j<n:
   cl[a[i+j]]+=1
   insort(h,a[i+j])
   x=h[pos[j]-1]
   f=cl[x]
   if cl[f]:c+=1
   j+=1
  i+=1
 print(c)

