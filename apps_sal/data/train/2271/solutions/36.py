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
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self):
        ret = dict()
        for i in range(self.n):
            x = self.find(i)
            if x in ret:
                ret[x].add(i)
            else:
                ret[x] = {i}
        return ret


N, M = map(int, input().split())
p = list(map(int, input().split()))
uf = UnionFind(N)
for _ in range(M):
    x, y = map(int, input().split())
    uf.union(x - 1, y - 1)
ans = 0
for id_s in uf.members().values():
    val_s = set()
    for i in id_s:
        val_s.add(p[i] - 1)
    ans += len(id_s & val_s)
print(ans)
