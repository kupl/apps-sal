'''
自宅用PCでの解答
'''
import math
import itertools
import queue
import bisect
from collections import deque, defaultdict
import heapq as hpq
from sys import stdin, setrecursionlimit
ipt = stdin.readline
setrecursionlimit(10**7)
mod = 10**9 + 7
dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
alp = "abcdefghijklmnopqrstuvwxyz"


class UnionFind():
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
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return set([i for i in range(self.n) if self.find(i) == root])

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return [self.members(r) for r in self.roots()]

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def main():
    n, m = list(map(int, ipt().split()))
    p = [int(i) - 1 for i in ipt().split()]
    uf = UnionFind(n)
    for i in range(m):
        x, y = list(map(int, ipt().split()))
        uf.union(x - 1, y - 1)

    ans = 0
    for i in range(n):
        if uf.same(i, p[i]):
            ans += 1

    print(ans)

    return None


def __starting_point():
    main()


__starting_point()
