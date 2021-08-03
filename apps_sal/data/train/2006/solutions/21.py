from fractions import gcd
from functools import reduce
n = int(input())
a = list(map(int, input().split()))
g = reduce(gcd, a)
s = max(a) // g - n
if s % 2:
    print('Alice')
else:
    print('Bob')
