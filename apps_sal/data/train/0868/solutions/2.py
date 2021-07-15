from math import ceil
def Beauty(array,f,n):
 i=0
 j=i
 ans=0
 while i<n and j<n:
  if array[j]==f:
   ans+=(n-j)*(j-i)+(n-j)
   i=j+1
   j=i
  else:
   j+=1
 return ans
from collections import defaultdict
for _ in range(int(input())):
 n,k=map(int,input().split( ))
 array=list(map(int,input().split( )))
 s=defaultdict(int)
 for v in array:
  s[v]+=1
 res=0
 for i in range(n):
  for j in range(i,n):
   b=array[i:j+1]
   b.sort()
   m=ceil(k/(j-i+1))
   t=ceil(k/m)
   x=b[t-1]
   f=b.count(x)
   if f in b:
    res+=1
   #res+=Beauty(array,f,n)
 print(res)
