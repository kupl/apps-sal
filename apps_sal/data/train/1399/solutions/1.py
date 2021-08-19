# cook your dish here
import sys
import math
from collections import Counter
from heapq import heapify, heappop, heappush
import numpy as np

# sys.setrecursionlimit(10**6)
# input = sys.stdin.buffer.readline

MAX_INT = 2**62 - 1
MOD = 10**9 + 7


def __starting_point():
    T = int(input())
    for _ in range(T):
        n, k = map(int, input().split())
        nums = np.array([int(s) for s in input().split()], dtype=np.int)
        ranges = []
        for _ in range(n):
            l, r = map(int, input().split())
            ranges.append((l - 1, r - 1))

        mat = np.zeros((n, n), dtype='u1')

        for i, (l, r) in enumerate(ranges):
            mat[i, l:r + 1] = 1

        trans = np.eye(n, dtype='u1')
        k -= 1
        while k:
            if k & 1:
                trans = trans @ mat
                trans &= 1
            k >>= 1
            mat = mat @ mat
            mat &= 1
            # print(k, trans)
        # print(trans)

        ans = np.zeros((n,), dtype=np.int)
        for i in range(60)[::-1]:
            c = (nums >> i) & 1
            ans <<= 1
            ans += (trans @ c & 1)
        print(*ans, sep=' ')


__starting_point()
