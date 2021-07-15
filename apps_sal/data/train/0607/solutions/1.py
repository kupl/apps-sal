MOD = 1000000007
MOD2 = 998244353
ii = lambda: int(input())
si = lambda: input()
dgl = lambda: list(map(int, input()))
f = lambda: map(int, input().split())
il = lambda: list(map(int, input().split()))
ls = lambda: list(input())
from math import gcd
for _ in range(ii()):
 n=ii()
 l=il()
 c=0
 g=0
 for i in range(n):
  g = gcd(g,l[i])
  if g==1:
   c+=1
   g=0
 print(c)
