# cook your dish here
import math
for _ in range(int(input())):
 n,m=map(int,input().split())
 if n==m or n==0 or m==0:
  print(n+m)
 else:
  x=math.gcd(n,m)
  print(2*x)
