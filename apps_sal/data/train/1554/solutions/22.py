# cook your dish here
from math import gcd
for _ in range(int(input())):
 x,y= map(int,input().split())
 if x==y:
  print(x+y)
 else:
  print(2*gcd(x,y))
