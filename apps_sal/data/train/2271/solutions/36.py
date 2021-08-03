class UnionFind:
    def __init__(self, n):
        # n: 頂点数
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        # xの根
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        # 無向辺をはる
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        # xの属する集団の頂点数
        return -self.parents[self.find(x)]

    def same(self, x, y):
        # 同集団に属するかどうか
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
# uf上のgroupごとに、groupのindexとその要素の積集合のサイズをとる
ans = 0
for id_s in uf.members().values():
    val_s = set()
    for i in id_s:
        val_s.add(p[i] - 1)
    ans += len(id_s & val_s)
    # print(id_s,val_s)
print(ans)
