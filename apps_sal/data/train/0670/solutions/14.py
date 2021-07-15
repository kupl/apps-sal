from fractions import gcd
from functools import reduce

t = int(input())
for tt in range(t):
 n = int(input())
 arr = list(map(int, input().split()))
 g = reduce(lambda x,y: gcd(x,y), arr)
 print(g * n)

