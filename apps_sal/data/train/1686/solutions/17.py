
import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2019/11/30 12:31

"""

R, C, D = map(int, input().split())


A = []
for r in range(R):
    A.append([int(x) for x in input().split()])


def solve1():
    if A[0][0] == 0:
        return 0
    MOD = 20011
    dp = [[0 for _ in range(C)] for _ in range(R)]
    dp[0][0] = 1
    for r in range(R):
        for c in range(C):
            if A[r][c] != 0:
                dp[r][c] += dp[r - 1][c] if r > 0 else 0
                dp[r][c] += dp[r][c - 1] if c > 0 else 0

    return dp[R - 1][C - 1]


def solve2():
    if A[0][0] == 0:
        return 0

    dp = [[[[0 for _ in range(D + 1)] for _ in range(2)] for _ in range(C)] for _ in range(R)]
    for c in range(1, min(C, D + 1)):
        if A[0][c] == 0:
            break
        dp[0][c][0][c] = 1
    for r in range(1, min(R, D + 1)):
        if A[r][0] == 0:
            break
        dp[r][0][1][r] = 1

    MOD = 20011
    for r in range(1, R):
        for c in range(1, C):
            if A[r][c] == 0:
                continue
            for d in range(2, D + 1):
                dp[r][c][0][d] = dp[r][c - 1][0][d - 1]
                dp[r][c][1][d] = dp[r - 1][c][1][d - 1]
                dp[r][c][0][d] %= MOD
                dp[r][c][1][d] %= MOD
            dp[r][c][0][1] = sum(dp[r][c - 1][1][1:]) % MOD
            dp[r][c][1][1] = sum(dp[r - 1][c][0][1:]) % MOD

    return (sum(dp[R - 1][C - 1][0]) + sum(dp[R - 1][C - 1][1])) % MOD


print(solve2())
