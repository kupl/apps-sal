from decimal import ROUND_HALF_UP, Decimal
from fractions import Fraction as frac
from itertools import combinations as com, permutations as per
from bisect import bisect_left as bileft, bisect_right as biright, insort
from functools import lru_cache
import sys
try:
    import os
    f = open('input.txt', 'r')
    sys.stdin = f
except FileNotFoundError:
    None
from math import sqrt, ceil, floor
from collections import deque, Counter, defaultdict
def input(): return sys.stdin.readline().strip()


sys.setrecursionlimit(11451419)

n, k = list(map(int, input().split()))
mod = 998244353

dp = [[0] * 3002 for i in range(3003)]
for i in range(1, n + 1):
    for j in range(n, 0, -1):
        if i < j:
            dp[i][j] = 0
        elif i == j:
            dp[i][j] = 1
        elif 2 * j > i:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = (dp[i - 1][j - 1] + dp[i][2 * j]) % mod

print((dp[n][k]))
