import sys
import math
import collections
import bisect
import copy
import itertools
sys.setrecursionlimit(10 ** 7)
INF = 10 ** 16
MOD = 10 ** 9 + 7


def ni():
    return int(sys.stdin.readline().rstrip())


def ns():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def na():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def na1():
    return list([int(x) - 1 for x in sys.stdin.readline().rstrip().split()])


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


def main():
    (n, m) = ns()
    p = na1()
    uf = UnionFind(n)
    for _ in range(m):
        (x, y) = ns()
        uf.union(x - 1, y - 1)
    ans = 0
    for (i, pi) in enumerate(p):
        if uf.same(i, pi):
            ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
