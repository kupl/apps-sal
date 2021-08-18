class union_find:
    def __init__(self, N):
        self.par = [-1] * N

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False
        else:
            if self.par[x] > self.par[y]:
                x, y = y, x
            self.par[x] += self.par[y]
            self.par[y] = x
            return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.par[self.find(x)]


N, M = map(int, input().split())
P = list(map(lambda x: int(x) - 1, input().split()))
uf = union_find(N)
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    uf.unite(x, y)

ans = 0
for i in range(N):
    if uf.same(P[i], i):
        ans += 1
print(ans)
