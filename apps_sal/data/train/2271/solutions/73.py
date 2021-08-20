import bisect
import heapq
import itertools
import sys
import math
import random
import time
from collections import Counter, deque, defaultdict
from functools import reduce
from operator import xor
from types import FunctionType
from typing import List
mod = 10 ** 9 + 7
sys.setrecursionlimit(10 ** 9)


def lmi():
    return list(map(int, input().split()))


def narray(*shape, init=0):
    if shape:
        num = shape[0]
        return [narray(*shape[1:], init=init) for _ in range(num)]
    return init


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
        for i in range(self.n):
            if self.find(i) == root:
                yield i

    def roots(self):
        for (i, x) in enumerate(self.parents):
            if x < 0:
                yield i

    def group_count(self):
        return len(list(self.roots()))

    def all_group_members(self):
        ret = defaultdict(list)
        for i in range(self.n):
            root = self.find(i)
            ret[root].append(i)
        return ret

    def __str__(self):
        return '\n'.join(('{}: {}'.format(r, list(members)) for (r, members) in self.all_group_members()))


def main():
    (N, M) = lmi()
    P = lmi()
    XY = [lmi() for _ in range(M)]
    uf = UnionFind(N)
    for (x, y) in XY:
        (x, y) = (x - 1, y - 1)
        uf.union(P[x] - 1, P[y] - 1)
    ans = 0
    for i in range(N):
        ans += uf.same(P[i] - 1, i)
    print(ans)


def __starting_point():
    main()


__starting_point()
