import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
'\ncreated by shhuan at 2019/11/30 21:18\n\n'
L = [int(x) for x in input().split()]
N = L[0]
K = L[1]
V = L[2:2 + N]
B = L[2 + N:]
bi = [[] for _ in range(20)]
L = []
for (i, v) in enumerate(B):
    bi[v].append(i)
    if v <= K:
        L.append(i)
dp = [[float('-inf') for _ in range(N + 1)] for _ in range(N)]
for i in range(N):
    dp[i][1] = 0
    dp[i][0] = 0
ans = 0
for l in range(2, N + 1):
    for s in range(N - l + 1):
        t = s + l - 1
        dp[s][l] = max(dp[s][l], dp[s][l - 1])
        pres = bi[B[t] - K]
        (pl, pr) = (bisect.bisect_left(pres, s), bisect.bisect_right(pres, t))
        for i in pres[pl:pr]:
            dp[s][l] = max(dp[s][l], V[i] + V[t] + dp[s][max(i - s, 0)] + dp[i + 1][max(t - i - 1, 0)])
            ans = max(ans, dp[s][l])
print(ans)
