import sys
import math
import io
import os
from bisect import bisect_left as bl, bisect_right as br, insort
from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter
from itertools import permutations, combinations
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var): sys.stdout.write(' '.join(map(str, var)) + '\n')
def out(var): sys.stdout.write(str(var) + '\n')


sys.setrecursionlimit(100000)
INF = float('inf')
mod = 998244353


n, k = mdata()
dp = [[0] * (n + 1) for i in range(n + 1)]
dp[0][0] = 1
dp[1][1] = 1
dp1 = [0] * (2 * n + 1)
for i in range(2, n + 1):
    for j in range(i, 0, -1):
        dp[i][j] = (dp[i - 1][j - 1] + dp1[2 * j]) % mod
        dp1[j] = dp[i][j] % mod
out(dp[n][k])
