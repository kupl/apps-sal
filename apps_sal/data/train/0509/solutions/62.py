import collections
N, M, *UVC = [int(_) for _ in open(0).read().split()]
U, V, C = [UVC[_::len('UVC')] for _ in range(len('UVC'))]
CUV = []
for u, v, c in zip(U, V, C):
    CUV += [(c, u, v)]
CUV.sort()


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1] * (n + 1)
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return 0
        elif self.rank[x] > self.rank[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.root[self.find(x)]


uf = UnionFind(N)
G = [{} for _ in range(N + 1)]
se = set()
for c, u, v in CUV:
    if uf.is_same(u, v):
        continue
    uf.unite(u, v)
    se.add(c)
    G[u][v] = G[v][u] = c
other = (set(range(1, N + 1)) - se).pop()
ans = [-1] * (N + 1)
ans[1] = 1
uf2 = UnionFind(N)
S = [1]
while S:
    u = S.pop()
    for v in G[u]:
        if uf2.is_same(u, v):
            continue
        uf2.unite(u, v)
        c = G[u][v]
        ans[v] = c if c != ans[u] else c % N + 1
        S += [v]
print(*ans[1:], sep='\n')
