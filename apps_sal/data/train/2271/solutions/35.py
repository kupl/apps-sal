import math
import itertools
import fractions
import heapq
import collections
import bisect
import sys
import queue
import copy
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20
mod = 10 ** 9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI():
    return [int(x) for x in sys.stdin.readline().split()]


def I():
    return int(sys.stdin.readline())


def F():
    return float(sys.stdin.readline())


def LS():
    return sys.stdin.readline().split()


def S():
    return input()


class UnionFind:

    def __init__(self, sz):
        self.sz = sz
        self.data = [-1] * sz
        self.amount = [0] * sz

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        self.amount[x] += self.amount[y]
        self.amount[y] += self.amount[x]
        if self.data[x] > self.data[y]:
            (x, y) = (y, x)
        self.data[x] += self.data[y]
        self.data[y] = x
        return True

    def find(self, k):
        if self.data[k] < 0:
            return k
        self.data[k] = self.find(self.data[k])
        return self.data[k]

    def size(self, k):
        return -self.data[self.find(k)]

    def set_amount(self, k, k_amount):
        self.amount[k] = k_amount

    def get_amount(self, k):
        return self.amount[k]


def main():
    (n, k) = LI()
    l = LI()
    d = {}
    uf = UnionFind(n)
    for (i, x) in enumerate(l):
        x -= 1
        d[i] = x
    for _ in range(k):
        (a, b) = LI()
        uf.unite(a - 1, b - 1)
    ans = 0
    for x in l:
        x -= 1
        if uf.find(x) == uf.find(d[x]):
            ans += 1
    return ans


print(main())
