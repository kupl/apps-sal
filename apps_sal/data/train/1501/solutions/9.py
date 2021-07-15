import sys
mod=10**9+7
n,q=list(map(int,input().split()))
u,l,r,d=1,n+1,n+1,pow(2,n,mod)
e=(2*(d-1))%mod
for a in sys.stdin:
 a=list(a.split())
 if a[0]=="1":
  e=(e*2)%mod
  if a[1]=="1":
   e=(e+r)%mod
   r=l
   u=(u*2)%mod
   d=(d*2)%mod
  elif a[1]=="2":
   e=(e+l)%mod
   l=r
   u=(u*2)%mod
   d=(d*2)%mod
  elif a[1]=="3": 
   e=(e+u)%mod
   u=d
   l=(l*2)%mod
   r=(r*2)%mod
  else:
   e=(e+d)%mod
   d=u
   l=(l*2)%mod
   r=(r*2)%mod
 else:
  print(e)
  

