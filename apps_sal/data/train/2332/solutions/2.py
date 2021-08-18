
from collections import defaultdict, deque
import sys
import heapq
import bisect
import math
import itertools
import string
import queue
import copy
import time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9 + 7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())


class UnionFind:
    def __init__(self, N):
        self.table = [i for i in range(N)]
        self.rank = [1 for i in range(N)]
        self.size = [1 for i in range(N)]

    def Find(self, x):
        if self.table[x] == x:
            return x
        else:
            self.table[x] = self.Find(self.table[x])
            self.size[x] = self.size[self.table[x]]
            return self.table[x]

    def Unite(self, x, y):
        x, y = self.Find(x), self.Find(y)
        sx, sy = self.Size(x), self.Size(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.table[y] = x
            self.size[x] = sx + sy
        else:
            self.table[x] = y
            self.size[y] = sx + sy
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def Check(self, x, y):
        return self.Find(x) == self.Find(y)

    def Size(self, x):
        return self.size[self.Find(x)]


for _ in range(inp()):
    N, M, a, b = inpl()
    a -= 1
    b -= 1
    a, b = min(a, b), max(a, b)
    UF = UnionFind(N)
    alines = []
    blines = []
    for _ in range(M):
        s, t = inpl()
        s -= 1
        t -= 1
        s, t = min(s, t), max(s, t)
        if s == a and t == b:
            continue
        elif s == a:
            alines.append(t)
        elif t == a:
            alines.append(s)
        elif s == b:
            blines.append(t)
        elif t == b:
            blines.append(s)
        else:
            UF.Unite(s, t)

    aconnects = set()
    acnts = [0] * N
    bcnts = [0] * N

    for a in alines:
        r = UF.Find(a)
        aconnects.add(r)
        acnts[r] = UF.Size(r)

    for b in blines:
        r = UF.Find(b)
        if r in aconnects:
            acnts[r] = 0
        else:
            bcnts[r] = UF.Size(r)

    print(sum(acnts) * sum(bcnts))
