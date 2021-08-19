class Uf:

    def __init__(self, N):
        self.p = list(range(N))
        self.rank = [0] * N
        self.size = [1] * N

    def root(self, x):
        if self.p[x] != x:
            self.p[x] = self.root(self.p[x])
        return self.p[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        u = self.root(x)
        v = self.root(y)
        if u == v:
            return
        if self.rank[u] < self.rank[v]:
            self.p[u] = v
            self.size[v] += self.size[u]
            self.size[u] = 0
        else:
            self.p[v] = u
            self.size[u] += self.size[v]
            self.size[v] = 0
            if self.rank[u] == self.rank[v]:
                self.rank[u] += 1

    def count(self, x):
        return self.size[self.root(x)]


(N, M) = map(int, input().split())
uf = Uf(N)
P = list(map(int, input().split()))
P = [i - 1 for i in P]
for i in range(M):
    (x, y) = map(int, input().split())
    x -= 1
    y -= 1
    uf.unite(x, y)
ans = 0
for i in range(N):
    if uf.root(P[i]) == uf.root(i):
        ans += 1
print(ans)
