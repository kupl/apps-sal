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
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20
eps = 1.0 / 10 ** 10
mod = 998244353
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LLI():
    return [list(map(int, l.split())) for l in sys.stdin.readlines()]


def LI_():
    return [int(x) - 1 for x in sys.stdin.readline().split()]


def LF():
    return [float(x) for x in sys.stdin.readline().split()]


def LS():
    return sys.stdin.readline().split()


def I():
    return int(sys.stdin.readline())


def F():
    return float(sys.stdin.readline())


def S():
    return input()


def pf(s):
    return print(s, flush=True)


def pe(s):
    return print(str(s), file=sys.stderr)


def JA(a, sep):
    return sep.join(map(str, a))


def main():
    n = I()
    aa = [LI() for _ in range(n - 1)]
    e = collections.defaultdict(set)
    for (a, b) in aa:
        e[a].add(b)
        e[b].add(a)
    q = [[(1, -1)]]
    qi = 0
    while 1:
        t = q[qi]
        nq = []
        for (i, p) in t:
            for c in e[i]:
                if c == p:
                    continue
                nq.append((c, i))
        if len(nq) < 1:
            break
        q.append(nq)
        qi += 1
    gm = [1]
    for i in range(1, n + 1):
        gm.append(i * gm[-1] % mod)
    m = {}

    def f(i, p):
        t = 1
        r = 1
        for c in e[i]:
            if c == p:
                continue
            r *= m[c]
            r %= mod
            t += 1
        if p == -1:
            r *= gm[t - 1]
            r *= n
        else:
            r *= gm[t]
        r %= mod
        m[i] = r
        return r
    for qt in q[::-1]:
        for (i, p) in qt:
            f(i, p)
    r = f(1, -1)
    return r


print(main())
