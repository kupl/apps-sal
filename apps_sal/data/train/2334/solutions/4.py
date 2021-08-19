import sys
import random
import math
import copy
from heapq import heappush, heappop, heapify
from functools import cmp_to_key
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
input = sys.stdin.readline


def getS():
    return input().strip()


def getN():
    return int(input())


def getList():
    return list(map(int, input().split()))


def getZList():
    return [int(x) - 1 for x in input().split()]


INF = float('inf')
MOD = 10 ** 9 + 7


def divide(x):
    return pow(x, MOD - 2, MOD)


def solve():
    S = getS()
    n = len(S)
    ans = 0
    bs = 0
    for c in reversed(S):
        if c == 'A':
            if bs:
                ans += 2
                bs -= 1
        else:
            bs += 1
    ans += bs // 2 * 2
    print(n - ans)


def main():
    n = getN()
    for _ in range(n):
        solve()
    return


def __starting_point():
    main()


__starting_point()
