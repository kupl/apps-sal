class UnionFind(object):

    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                (x, y) = (y, x)
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x

    def is_same(self, x, y):
        return self.find(x) == self.find(y)


(n, m) = map(int, input().split())
uf1 = UnionFind(n)
p = list(map(int, input().split()))
for i in range(m):
    (a, b) = map(int, input().split())
    uf1.union(a - 1, b - 1)
for i in range(n):
    uf1.find(i)
ans = 0
for i in range(n):
    if uf1.par[i] == uf1.par[p[i] - 1]:
        ans += 1
print(ans)
