from itertools import permutations
from bisect import bisect_left as bl, bisect_right as br
from collections import defaultdict as dd, Counter
from math import ceil
from math import gcd
import sys
INF = 10**20
MOD = 10**9 + 7
def I(): return list(map(int, input().split()))

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
