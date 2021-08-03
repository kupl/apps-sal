from collections import defaultdict
import sys
input = sys.stdin.readline


class Unionfind:
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [1] * n

    def root(self, x):
        p = x

        while not self.par[p] < 0:
            p = self.par[p]

        while x != p:
            tmp = x
            x = self.par[x]
            self.par[tmp] = p

        return p

    def unite(self, x, y):
        rx, ry = self.root(x), self.root(y)

        if rx == ry:
            return False

        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx

        self.par[rx] += self.par[ry]
        self.par[ry] = rx

        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def count(self, x):
        return -self.par[self.root(x)]


n = int(input())
a = list(map(int, input().split()))
b = a[:]
b.sort()
d = defaultdict(int)

for i in range(n):
    d[b[i]] = i

uf = Unionfind(n)

for i in range(n):
    uf.unite(i, d[a[i]])

ans = defaultdict(list)

for i in range(n):
    ans[uf.root(i)].append(i)

print(len(list(ans.keys())))

for l in ans.values():
    print(len(l), *list(map(lambda x: x + 1, l)))
