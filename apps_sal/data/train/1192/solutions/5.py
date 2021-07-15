# cook your dish here
import math
from collections import defaultdict
t=int(input())
for i in range(t):
 n=int(input())
 b=list(map(int,input().split()))
 j=0
 res=[]
 while(j<n):
  if math.gcd(b[j],b[(j+1)%n])>1:
   res.append(1)
  else:
   res.append(0)
  j+=1
 j=0
 f=0
 ans=[]
 while(j<n):
  if res[j]==0:
   f=1
   req=j
   break
  j+=1
 if f==0:
  j=1
  while(j<n):
   ans.append(math.ceil(n/j))
   j+=1
  print(*ans)

 else:
  j=req+1
  s=0
  while(j%n!=req):
   if res[j%n]==1:
    s+=1
   else:
    if s!=0:
     ans.append(s)
    s=0
   j+=1
  ans.append(s)
  d=defaultdict(lambda:0)
  j=0
  l=len(ans)

  while(j<l):
   p=ans[j]
   r=p
   while(r>=1):
    d[r]+=(p//r)
    r+=-1
   j+=1
  ans=[]
  r=1
  while(r<n):
   ans.append(d[r])
   r+=1
  print(*ans)
























