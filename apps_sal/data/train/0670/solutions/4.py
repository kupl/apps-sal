from fractions import *
for _ in range(int(input())):
 n=int(input())
 a=list(map(int,input().split()))
 q=a[0]
 for i in range(1,n):
  q=gcd(a[i],q)
  if q==1:
   break
 print(q*n)
