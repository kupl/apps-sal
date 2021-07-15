from math import *
t=int(input())
while t:
 n=int(input())
 p=sqrt(n)
 if p*p==n:
  print("YES")
 else:
  print("NO")
 t-=1
