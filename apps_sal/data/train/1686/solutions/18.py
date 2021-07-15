# -*- coding: utf-8 -*-

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
# import random

R, C, D = map(int, input().split())
#
# R, C, D = 5, 5, 15

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
                dp[r][c] += dp[r-1][c] if r > 0 else 0
                dp[r][c] += dp[r][c-1] if c > 0 else 0
                dp[r][c] %= MOD

    # for row in dp:
    #     print(row)

    return dp[R-1][C-1]

def solve2():
    if A[0][0] == 0:
        return 0

    dp = [[[[0 for _ in range(D+1)] for _ in range(2)] for _ in range(C)] for _ in range(R)]

    if A[0][1] != 0:
        dp[0][1][0][1] = 1
    if A[1][0] != 0:
        dp[1][0][1][1] = 1

    A[0][1] = 0
    A[1][0] = 0

    MOD = 20011
    for r in range(R):
        for c in range(C):
            if A[r][c] == 0:
                continue
            for d in range(2, D+1):
                dp[r][c][0][d] += dp[r][c-1][0][d-1] if c > 0 else 0
                dp[r][c][1][d] += dp[r-1][c][1][d-1] if r > 0 else 0
                dp[r][c][0][d] %= MOD
                dp[r][c][1][d] %= MOD
            dp[r][c][0][1] = (sum(dp[r][c-1][1][1:]) if c > 0 else 0) % MOD
            dp[r][c][1][1] = (sum(dp[r-1][c][0][1:]) if r > 0 else 0) % MOD


    # for r in range(R):
    #     for c in range(C):
    #         print('='*10 + '{}-{}'.format(r, c)+'='*10)
    #         for row in dp[r][c]:
    #             print(row)

    return sum(dp[R-1][C-1][0]) + sum(dp[R-1][C-1][1]) % MOD

# while True:
#     R, C = random.randint(2, 10), random.randint(2, 10)
#     A = []
#     for i in range(R):
#         # A.append([int(x) for x in input().split()])
#         A.append([1 if random.randint(1, 10) > 2 else 0 for _ in range(C)])
#
#     R, C = len(A), len(A[0])
#     a, b = solve1(), solve2()
#     print(a, b)
#     if a != b:
#         for row in A:
#             print(row)
#         print('=' * 40)
#         print(a, b)
#         exit(0)

print(solve1())
