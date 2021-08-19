"""

created by shuangquan.huang at 1/9/20

"""
import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def check(H, N, K):
    for i in range(K + 1, N - K + 1):
        h = H[i]
        for j in range(K + 1):
            if h <= 0:
                break
            if i - j >= 0:
                h = min(h, H[i - j] - (K - j))
            if i + j <= N:
                h = min(h, H[i + j] - (K - j))
        if h > 0:
            return False
    return True


def solve2(N, A):
    A = [0] + A + [0]
    (lo, hi) = (0, N // 2 + 1)
    while lo <= hi:
        k = (lo + hi) // 2
        if check(A, N, k):
            hi = k - 1
        else:
            lo = k + 1
    return lo


def solve(N, A):
    A = [0] + A + [0]
    H = [N] * (N + 2)
    H[0] = H[-1] = 0
    worst = 0
    for i in range(1, N + 1):
        worst = min(worst, A[i] - i)
        H[i] = i + worst
    worst = N + 1
    for i in range(N, 0, -1):
        worst = min(worst, A[i] + i)
        H[i] = min(H[i], worst - i)
    return max(H)


N = int(input())
A = [int(x) for x in input().split()]
print(solve(N, A))
