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
import copy
import functools
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20
gosa = 1.0 / 10 ** 10
mod = 10 ** 9 + 7


def LI():
    return [int(x) for x in sys.stdin.readline().split()]


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


class Seg:

    def __init__(self, na, default, func):
        if isinstance(na, list):
            n = len(na)
        else:
            n = na
        i = 1
        while 2 ** i <= n:
            i += 1
        self.D = default
        self.H = i
        self.N = 2 ** i
        if isinstance(na, list):
            self.A = [default] * self.N + na + [default] * (self.N - n)
            for i in range(self.N - 1, 0, -1):
                self.A[i] = func(self.A[i * 2], self.A[i * 2 + 1])
        else:
            self.A = [default] * (self.N * 2)
        self.F = func

    def find(self, i):
        return self.A[i + self.N]

    def update(self, i, x):
        i += self.N
        self.A[i] = x
        while i > 0:
            i = (i - 1) // 2
            self.A[i] = self.merge(self.A[i * 2], self.A[i * 2 + 1])

    def merge(self, a, b):
        return self.F(a, b)

    def total(self):
        return self.A[0]

    def query(self, a, b):
        A = self.A
        l = a + self.N
        r = b + self.N
        res = self.D
        while l < r:
            if l % 2 == 1:
                res = self.merge(res, A[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                res = self.merge(res, A[r])
            l >>= 1
            r >>= 1
        return res


def main():
    n = I()
    a = LI()

    def sf(a, b):
        if a < b:
            return a
        return b
    s1 = Seg([c if i % 2 == 0 else inf for (c, i) in zip(a, list(range(n)))], inf, sf)
    s2 = Seg([c if i % 2 == 1 else inf for (c, i) in zip(a, list(range(n)))], inf, sf)
    d = {}
    for i in range(n):
        d[a[i]] = i

    def f(l, r):
        if l % 2 == 0:
            t = s1.query(l, r)
            ti = d[t]
            u = s2.query(ti + 1, r)
        else:
            t = s2.query(l, r)
            ti = d[t]
            u = s1.query(ti + 1, r)
        ui = d[u]
        nl = []
        if l < ti:
            nl.append((l, ti))
        if ui - ti > 1:
            nl.append((ti + 1, ui))
        if ui < r - 1:
            nl.append((ui + 1, r))
        return ((t, u), nl)
    q = []
    heapq.heappush(q, f(0, n))
    r = []
    while q:
        (t, nl) = heapq.heappop(q)
        r.append(t[0])
        r.append(t[1])
        for (t, u) in nl:
            heapq.heappush(q, f(t, u))
    return ' '.join(map(str, r))


print(main())
