#!/usr/bin/env python

from sys import stdin


def Choose(n, k):
    if n < 0 or k < 0 or k > n:
        return 0
    if k > n - k:
        k = n - k
    res = 1
    for i in range(1, k + 1):
        res = res * (n - i + 1) / i
    return res


TC = int(stdin.readline().strip())
for tc in range(TC):
    N, K = list(map(int, stdin.readline().split()))
    print(Choose(N, K))
