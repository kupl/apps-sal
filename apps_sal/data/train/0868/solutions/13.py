import bisect
import math
t=int(input())
while t>0:
 fp=0
 n,k=map(int,input().split())
 a=list(map(int,input().split()))
 
 for i in range(n):
  left=[]
  
  arr=[0]*2005
  for j in range(i,n):
   bisect.insort(left, a[j])
   arr[a[j]]+=1
   uhoy=math.ceil(k/(j-i+1))
   mc=int(((k-1)/uhoy))
   kpop=arr[left[mc]]
   if arr[kpop]>=1:
    fp+=1
 print(fp)
 t-=1
