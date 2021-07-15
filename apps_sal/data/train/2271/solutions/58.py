import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, M = mapint()
Ps = [p-1 for p in list(mapint())]

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
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

uf = UnionFind(N)
for _ in range(M):
    x, y = mapint()
    uf.union(x-1, y-1)

roots = uf.roots()
root_set = [set() for _ in range(N)]

for i in range(N):
    root_set[uf.find(i)].add(i)

ans = 0
for i in range(N):
    p = Ps[i]
    if p in root_set[uf.find(i)]:
        ans += 1
print(ans)
