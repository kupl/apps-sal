
import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2019/11/30 21:18

"""

L = [int(x) for x in input().split()]

N = L[0]
K = L[1]
V = L[2: 2 + N]
B = L[2 + N:]


bi = collections.defaultdict(list)
for i, v in enumerate(B):
    bi[v].append(i)


memo = {}


def dfs(l, r):
    if l >= r:
        return 0

    k = (l, r)
    if k in memo:
        return memo[k]

    ans = 0
    for i in range(l, r):
        for j in bi[B[i] + K]:
            if i < j <= r:
                ans = max(ans, V[i] + V[j] + dfs(i + 1, j - 1) + dfs(j + 1, r))
    memo[k] = ans

    return ans


print(dfs(0, N - 1))
