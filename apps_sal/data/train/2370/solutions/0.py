#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return [list(x) for x in sys.stdin.readline().split()]


def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res


def IR(n):
    return [I() for i in range(n)]


def LIR(n):
    return [LI() for i in range(n)]


def SR(n):
    return [S() for i in range(n)]


def LSR(n):
    return [LS() for i in range(n)]


sys.setrecursionlimit(1000000)
mod = 1000000007


def solve():
    def f(a, b):
        if a == b:
            return len(d[a])
        da = d[a]
        db = d[b]
        res = 0
        for x in range(len(da) >> 1):
            l = da[x]
            r = da[-1 - x]
            i = bisect.bisect_left(db, l)
            j = bisect.bisect_left(db, r)
            y = max(0, j - i)
            s = 2 * (x + 1) + y
            if res < s:
                res = s
        return res

    t = I()
    for _ in range(t):
        n = I()
        a = LI()
        m = max(a)
        d = [[] for i in range(m)]
        for i in range(n):
            ai = a[i] - 1
            d[ai].append(i)
        ans = 1
        for a in range(m):
            if not d[a]:
                continue
            for b in range(m):
                if not d[b]:
                    continue
                res = f(a, b)
                if ans < res:
                    ans = res
        print(ans)
    return

# Solve


def __starting_point():
    solve()


__starting_point()
