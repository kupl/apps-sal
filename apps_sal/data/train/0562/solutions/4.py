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
created by shhuan at 2018/10/30 19:45

"""


N, M = map(int, input().split())

A = []

for i in range(N):
    A.append([int(x) for x in input()])

# for row in A:
#     print(row)


# f(r, c, color, width) = f(r+1, c+1, color, width-1) + mismatches_in_edge

mxMN, mnMN = max(M, N), min(M, N)
ans = [float('inf') for _ in range(mxMN + 1)]
f = [[[[0 for _ in range(mxMN + 1)] for color in range(2)] for c in range(M + 1)] for r in range(N + 1)]

for width in range(1, min(N, N) + 1):
    for color in [0, 1]:
        for sr in range(N - width + 1):
            for sc in range(N - width + 1):
                steps = f[sr + 1][sc + 1][color][width - 1]

                cc = color
                for c in range(sc, sc + width):
                    steps += 0 if A[sr][c] == cc else 1
                    cc ^= 1
                cc = color ^ 1
                for r in range(sr + 1, sr + width):
                    steps += 0 if A[r][sc] == cc else 1
                    cc ^= 1

                f[sr][sc][color][width] = steps
                ans[width] = min(ans[width], steps)

qc = input()
qs = [int(x) for x in input().split()]

# print()
# print(ans)
for q in qs:
    print(bisect.bisect_right(ans, q) - 1)
