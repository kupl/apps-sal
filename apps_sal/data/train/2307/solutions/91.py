import sys
import os
from copy import copy
import operator
import time
import datetime
import math
from math import floor, ceil, sqrt, log
import statistics
from statistics import mean, median
from decimal import Decimal as D
from fractions import Fraction as F
import functools
import random
from random import randint, shuffle
import bisect
import string
from collections import deque
import collections
import itertools
import heapq
sys.setrecursionlimit(4100000)
product = functools.partial(functools.reduce, operator.mul)
INF = float('inf')


class UnionFind:

    def __init__(self, n):
        self.parents = [-1] * n

    def union(self, x, y):
        (x, y) = (self.find(x), self.find(y))
        if x != y:
            if self.parents[x] > self.parents[y]:
                (x, y) = (y, x)
            self.parents[x] += self.parents[y]
            self.parents[y] = x

    def find(self, x):
        if self.parents[x] < 0:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return list(filter(lambda x: x < 0, self.parents))

    def group_count(self):
        return len(self.roots())

    def max_size(self):
        return -min(self.parents)

    def min_size(self):
        return -max(self.roots())

    def append(self, n):
        self.parents += [-1] * n


class Imos:

    def __init__(self, n):
        self.val = [0] * n

    def add(self, x, y, n=None):
        if n is None:
            n = 1
        self.val[x] += n
        if len(self.val) > y + 1:
            self.val[y + 1] -= n

    def imos(self):
        for i in range(1, len(self.val)):
            self.val[i] += self.val[i - 1]

    def max(self):
        return max(self.val)

    def min(self):
        return min(self.val)


class CS:

    def __init__(self, grid):
        self.cs = grid
        for i0 in range(len(grid)):
            for i1 in range(len(grid[0])):
                if i0 == 0:
                    if i1 == 0:
                        continue
                    self.cs[i0][i1] += self.cs[i0][i1 - 1]
                elif i1 == 0:
                    self.cs[i0][i1] += self.cs[i0 - 1][i1]
                else:
                    self.cs[i0][i1] += self.cs[i0 - 1][i1] + self.cs[i0][i1 - 1] - self.cs[i0 - 1][i1 - 1]

    def sum(self, start_0, start_1, end_0, end_1):
        if start_0 == 0:
            if start_1 == 0:
                return self.cs[end_0][end_1]
            return self.cs[end_0][end_1] - self.cs[end_0][start_1 - 1]
        if start_1 == 0:
            return self.cs[end_0][end_1] - self.cs[start_0 - 1][end_1]
        start_0 -= 1
        start_1 -= 1
        return self.cs[end_0][end_1] - self.cs[start_0][end_1] - self.cs[end_0][start_1] + self.cs[start_0][start_1]


def mod(n):
    return n % (10 ** 9 + 7)


def sinput():
    return sys.stdin.readline()[:-1]


def input():
    inputs = list(map(int, sys.stdin.readline().split()))
    if len(inputs) == 1:
        return inputs[0]
    return inputs


def listban(l):
    return list(map(list, set(map(tuple, l))))


def div(n):
    (lower_divisors, upper_divisors) = ([], [])
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def prime(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def div_counter(l, n):
    return prime(l).count(n)


def lcm(x, y):
    return x * y // math.gcd(x, y)


def C(n, r):
    if n < r:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def P(n, r):
    if n < r:
        return 0
    return math.factorial(n) // math.factorial(n - r)


def H(n, r):
    return C(n + r - 1, r)


def cos(x, y, a):
    return (x ** 2 + y ** 2 - 2 * x * y * math.cos(math.radians(a))) ** 0.5


def DFS(g, s, pos=None):
    if pos is None:
        pos = set()
    pos.add(s)
    for i in g[s]:
        if not i in pos:
            DFS(g, i, pos)
    return pos


def DFS_one(g, s, pos=None):
    if pos is None:
        pos = set()
    pos = copy(pos)
    pos.add(s)
    b = copy(pos)
    m = copy(pos)
    for i in g[s]:
        if not i in pos:
            b = DFS(g, i, pos)
            if len(m) < len(b):
                m = b
    return m


def BFS(g, q, pos=None):
    if pos is None:
        pos = set()
    if type(q) == deque:
        pos.add(q)
        q = deque([q])
    pos.add(q[-1])
    for i in g[q.pop()]:
        if not i in pos:
            q.append(i)
    while q != deque():
        (pos, q) = BFS(g, q, pos)
    return (pos, q)


def SSP(a, li=None):
    if li is None:
        li = []
    if len(a) == 1:
        return [a[0]]
    return list(set(li + SSP(a[1:], li) + list(map(lambda x: x + a[0], SSP(a[1:], li))) + [a[0]]))


def dijkstra(g, s):
    n = len(g)
    dist = [10 ** 100] * n
    hq = [(0, s)]
    dist[s] = 0
    seen = [False] * n
    while hq:
        v = heapq.heappop(hq)[1]
        seen[v] = True
        for (to, cost) in g[v]:
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heapq.heappush(hq, (dist[to], to))
    return dist


def LIS(b):
    l = [b[0]]
    for i in b:
        if i > l[-1]:
            l += [i]
        else:
            l[bisect.bisect_left(l, i)] = i
    return len(l)


def two(n):
    return len(str(bin(n))) - str(bin(n)).rfind('1') - 1


def yn(b):
    if b:
        print('Yes')
    else:
        print('No')


def op(s):
    print(s)
    return ()


(n, a, b) = input()
x = input()
ans = 0
for i in range(1, n):
    ans += min((x[i] - x[i - 1]) * a, b)
print(ans)
