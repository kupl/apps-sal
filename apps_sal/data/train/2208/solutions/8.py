class UnionFind:

    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1] * n
        self.edge = [0] * n
        self.rank = [0] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.size[self.find(x)]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            self.edge[x] += 1
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
            self.edge[y] += self.edge[x] + 1
        else:
            self.par[y] = x
            self.size[x] += self.size[y]
            self.edge[x] += self.edge[y] + 1
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


(n, k) = [int(item) for item in input().split()]
UF = UnionFind(2 * 10 ** 5)
for i in range(k):
    (a, b) = [int(item) for item in input().split()]
    a -= 1
    b -= 1
    UF.union(a, b)
seen = [False] * (2 * 10 ** 5)
ans = 0
for i in range(2 * 10 ** 5):
    par = UF.find(i)
    if seen[par]:
        continue
    if UF.edge[par] == 0:
        continue
    else:
        ans += UF.edge[par] - (UF.size[par] - 1)
    seen[par] = True
print(ans)
