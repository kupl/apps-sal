from sys import stdin,stdout
from math import gcd
nmbr=lambda:int(stdin.readline())
lst=lambda:list(map(int, stdin.readline().split()))

for _ in range(nmbr()):
 n=nmbr()
 a=lst()
 g=a[0]
 ans=0
 for v in a[1:]:
  g=gcd(v,g)
 for i in a:
  ans+=i//g
 print(g,ans)
