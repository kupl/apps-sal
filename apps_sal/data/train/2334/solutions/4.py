import sys
import random
# import numpy as np
import math
import copy
from heapq import heappush, heappop, heapify
from functools import cmp_to_key
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter

# sys.setrecursionlimit(1000000)
# input aliases
input = sys.stdin.readline
getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = float("inf")

MOD = 10 ** 9 + 7
divide = lambda x: pow(x, MOD - 2, MOD)


def solve():
    S = getS()
    n = len(S)

    ans = 0
    bs = 0
    for c in reversed(S):
        if c == "A":
            if bs:
                ans += 2
                bs -= 1
        else:
            bs += 1

    ans += (bs // 2) * 2

    print(n - ans)

def main():
    n = getN()
    for _ in range(n):
        solve()

    return


def __starting_point():
    main()
    # solve()

__starting_point()
