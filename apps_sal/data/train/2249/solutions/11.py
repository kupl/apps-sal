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
def getS(): return input().strip()
def getN(): return int(input())
def getList(): return list(map(int, input().split()))
def getZList(): return [int(x) - 1 for x in input().split()]


INF = float("inf")

MOD = 10 ** 9 + 7
def divide(x): return pow(x, MOD - 2, MOD)


def solve():
    a, b, x, y = getList()
    if a == x:
        print(abs(b - y))
        return
    if b == y:
        print(abs(a - x))
        return

    print(abs(a - x) + abs(b - y) + 2)


def main():
    n = getN()
    for _ in range(n):
        solve()

    return


def __starting_point():
    main()
    # solve()


__starting_point()
