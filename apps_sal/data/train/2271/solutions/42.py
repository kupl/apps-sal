N, M = list(map(int, input().split()))
p = list(map(int, input().split()))

pairs = [list(map(int, input().split())) for _ in range(M)]


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]

    def root(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        self.par[x] = y

    def check(self, x, y):
        return self.root(x) == self.root(y)


u = UnionFind(N)

for x, y in pairs:
    u.union(x, y)

ans = 0
for j in range(1, N + 1):
    if u.check(p[j - 1], j):
        ans += 1
print(ans)

