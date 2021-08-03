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
import random
import time

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7


def LI(): return list(map(int, input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()


def main():
    n = II()
    d = collections.defaultdict(set)
    for _ in range(n - 1):
        a, b = LI()
        d[a].add(b)
        d[b].add(a)

    memo = [-1] * (n + 1)

    def path(t, s):
        ps = set()
        dt = list(d[t])
        for k in dt:
            if memo[k] < 0:
                continue
            ps.add(memo[k])

        if s == -1 and len(ps) == 2:
            memo[t] = sum(ps) + 2
            return memo[t]

        if len(ps) > 1:
            return -t

        if len(ps) == 0:
            memo[t] = 0
            return 0

        memo[t] = list(ps)[0] + 1
        return memo[t]

    def _path(tt, ss):
        q = [(tt, ss)]
        tq = []
        qi = 0
        while len(q) > qi:
            t, s = q[qi]
            for k in d[t]:
                if k == s:
                    continue
                q.append((k, t))
            qi += 1
        for t, s in q[::-1]:
            r = path(t, s)
            if r < 0:
                return r
        return memo[tt]

    def _path2(tt, ss):
        q = [(tt, ss)]
        tq = []
        qi = 0
        while len(q) > qi:
            t, s = q[qi]
            for k in d[t]:
                if k == s or memo[k] >= 0:
                    continue
                q.append((k, t))
            qi += 1
        for t, s in q[::-1]:
            r = path(t, s)
            if r < 0:
                return r
        return memo[tt]

    t = _path(1, -1)
    if t < 0:
        t = _path2(-t, -1)

    if t > 0:
        while t % 2 == 0:
            t //= 2
        return t

    return -1


print(main())
