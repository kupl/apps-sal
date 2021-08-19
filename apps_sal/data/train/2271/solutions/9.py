(N, M) = map(int, input().split())
(*P,) = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(M)]


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


uf = UnionFind(N)
for (x, y) in xy:
    uf.union(x - 1, y - 1)
ans = sum((uf.find(i) == uf.find(P[i] - 1) for i in range(N)))
print(ans)
