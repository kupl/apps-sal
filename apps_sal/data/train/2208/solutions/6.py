import sys


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1
            elif self.rank[px] < self.rank[py]:
                px, py = py, px
            self.par[py] = px
            self.size[px] += self.size[py]

    def same_check(self, x, y):
        return self.find(x) == self.find(y)


input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n, k = map(int, input().split())
uf = UnionFind(n)
Edges = set()
for _ in range(k):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if a > b:
        a, b = b, a
    Edges.add((a, b))
for a, b in Edges:
    uf.union(a, b)
P = set()
for i in range(n):
    P.add(uf.find(i))
num = 0
for p in P:
    num += uf.size[p] - 1
print(k - num)
