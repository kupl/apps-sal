# cook your dish here
import math
t=int(input())
while t>0:
 n,l=list(map(int,input().split()))
 if n==1:
  print(l)
 elif n==2:
  ans=math.sqrt(l)
  k=int(ans)
  if k*k==ans:
   print(k)
  else:
   print(k+1)
   
 t-=1
