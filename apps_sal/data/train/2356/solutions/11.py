import sys
import bisect
import math
import itertools
import heapq
import collections
from operator import itemgetter
from functools import lru_cache
import copy
input = sys.stdin.readline
INF = float('inf')
mod = 10 ** 9 + 7
eps = 10 ** (-7)


def inp():
    """
    一つの整数
    """
    return int(input())


def inpl():
    """
    一行に複数の整数
    """
    return list(map(int, input().split()))


def str_inp():
    """
    文字列をリストとして読み込む
    """
    return list(input()[:-1])


mod = 998244353
(n, k) = inpl()
dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, i + 1)[::-1]:
        if i == j:
            dp[i][j] = 1
            continue
        a = dp[i - 1][j - 1]
        b = dp[i][2 * j] if 2 * j < n + 1 else 0
        dp[i][j] = (a + b) % mod
print(dp[n][k] % mod)
