import sys
import math
import collections
import heapq
import queue
import itertools
import functools
import operator
import time

readline = sys.stdin.readline


def IPS(): return readline().rstrip()
def IP(): return int(readline().rstrip())
def MP(): return map(int, readline().split())
def LS(): return list(map(int, readline().split()))
def AR(): return [int(x) for x in readline().split()]


def solve():
    for _ in range(IP()):
        n, k = MP()

        ans = [-x for x in range(1, n + 1)]

        ans[0] = -ans[0]
        k -= 1

        i, j = 1, -1
        if n & 1 == 1:
            j = n - 1
        else:
            j = n - 2

        while k > 0:
            if(i < n):
                ans[i] = -ans[i]
                i += 2
            elif j > 0:
                ans[j] = -ans[j]
                j -= 2
            k -= 1

        for a in ans:
            print(a, end=" ")
        print()


def __starting_point():
    solve()


__starting_point()
