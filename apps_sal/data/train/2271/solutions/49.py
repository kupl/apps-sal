from collections import defaultdict, deque
import sys
import heapq
import bisect
import math
import itertools
import string
import queue
import datetime


def inpl():
    return list(map(int, input().split()))


def inpl_s():
    return list(input().split())


class UnionFind:

    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            (x, y) = (y, x)
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for (i, x) in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join(('{}: {}'.format(r, self.members(r)) for r in self.roots()))


(N, M) = map(int, input().split())
p = inpl()
uf = UnionFind(N)
for i in range(M):
    (x, y) = map(int, input().split())
    x -= 1
    y -= 1
    uf.union(x, y)
ans = 0
for i in range(N):
    if uf.same(p[i] - 1, i):
        ans += 1
print(ans)
