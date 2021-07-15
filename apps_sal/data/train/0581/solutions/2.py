from math import *
t=int(input())
for i in range(t):
 a=list(map(float,input().split()))
 b=list(map(float,input().split()))
 c=sum(b)+a[2]
 d=float(a[1]/c)
 if ceil(d)==d:
  print("YES")
 else:
  print("NO")

