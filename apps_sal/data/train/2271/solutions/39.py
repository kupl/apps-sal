import operator
import itertools
import collections
import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))
def nn(): return list(stdin.readline().split())
def ns(): return stdin.readline().rstrip()


class UnionFind:
    def __init__(self, elems=None):
        class KeyDict(dict):
            def __missing__(self, key):
                self[key] = key
                return key

        self.parent = KeyDict()
        self.rank = collections.defaultdict(int)
        self.size_ = collections.defaultdict(lambda: 1)

        if elems is not None:
            for elem in elems:
                _, _, _ = self.parent[elem], self.rank[elem], self.size_[elem]

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
            self.size_[y] += self.size_[x]
        else:
            self.parent[y] = x
            self.size_[x] += self.size_[y]
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

    def are_same(self, x, y):
        return self.find(x) == self.find(y)

    def grouper(self):
        roots = [(x, self.find(x_par)) for x, x_par in self.parent.items()]
        root = operator.itemgetter(1)
        for _, group in itertools.groupby(sorted(roots, key=root), root):
            yield [x for x, _ in group]

    def size(self, x):
        return self.size_[self.find(x)]


n, m = na()
p = na()
uf = UnionFind()
for i in range(m):
    x, y = na()
    uf.unite(x, y)

dp = []
for i in range(n):
    dp.append(uf.find(i + 1))

ans = 0
for i in range(n):
    if dp[i] == uf.find(p[i]) or i + 1 == p[i]:
        ans += 1

print(ans)
