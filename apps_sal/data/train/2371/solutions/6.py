import sys
INF = 10**20
MOD = 10**9 + 7
I = lambda:list(map(int,input().split()))
from math import gcd
from math import ceil
from collections import defaultdict as dd, Counter
from bisect import bisect_left as bl, bisect_right as br
from itertools import permutations

"""
Facts and Data representation
Constructive? Top bottom up down
"""
def solve():
  n, = I()
  a = I()
  j = n - 1
  while j > 0 and a[j - 1] >= a[j]:
    j -= 1
  mx = a[j]
  while j > 0 and a[j - 1] <= a[j] and a[j - 1] <= mx:
    j -= 1
  print(j)

t, = I()
while t:
  t -= 1
  solve()
