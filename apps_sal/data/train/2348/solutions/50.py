import bisect
import os
import sys

import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))
L = int(sys.stdin.readline())
Q = int(sys.stdin.readline())
AB = [list(map(int, sys.stdin.readline().split())) for _ in range(Q)]

N += 2
X = [X[0]] + X + [X[-1]]
X = np.array(X, dtype=int)
# dp[d][i]: i番のホテルから(2^d)日で何個右までいけるか
dp = np.zeros((N, N.bit_length() + 1), dtype=int)
dp[:, 0] = np.searchsorted(X, X + L, side="right") - 1
for d in range(1, N.bit_length() + 1):
    dp[:, d] = dp[dp[:, d - 1], d - 1]
dp = dp.tolist()


def solve(l, r):
    ret = 0
    while l + 1 < r:
        d = max(0, bisect.bisect_left(dp[l], r) - 1)
        ret += pow(2, d)
        l = dp[l][d]
    if l < r:
        ret += 1
    return ret


ans = []
for a, b in AB:
    ans.append(solve(min(a, b), max(a, b)))
print(*ans, sep='\n')
