import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import copy
import functools
import time
import random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9 + 7
mod2 = 998244353
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def pe(s): return print(str(s), file=sys.stderr)
def JA(a, sep): return sep.join(map(str, a))
def JAA(a, s, t): return s.join(t.join(map(str, b)) for b in a)


def main():
    n, q = LI()
    stx = [LI() for _ in range(n)]
    da = [I() for _ in range(q)]

    q = []
    for s, t, x in stx:
        sx = s - x
        tx = t - x - 1
        heapq.heappush(q, (sx, x, tx))

    t = []
    cx = inf
    ctx = inf
    c = 0
    while len(q):
        sx, x, tx = heapq.heappop(q)
        if sx > ctx:
            t.append((sx - 1, cx))
            cx = x
            ctx = tx
        elif cx > x:
            if ctx > tx:
                heapq.heappush(q, (tx + 1, cx, ctx))
            t.append((sx - 1, cx))
            cx = x
            ctx = tx
        elif tx > ctx:
            heapq.heappush(q, (ctx + 1, x, tx))

    t.append((inf, inf))

    r = []
    for d in da:
        i = bisect.bisect_right(t, (d, -1))
        u = t[i][1]
        if u == inf:
            r.append(-1)
        else:
            r.append(u)

    return JA(r, "\n")


print(main())
