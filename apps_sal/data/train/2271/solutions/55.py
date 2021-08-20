(n, m) = map(int, input().split())
P = [i - 1 for i in list(map(int, input().split()))]


class UnionFind:

    def __init__(self, num):
        self.n = num
        self.parents = [-1 for i in range(self.n)]

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        xx = self.find(x)
        yy = self.find(y)
        if xx == yy:
            return
        else:
            size_xx = abs(self.parents[xx])
            size_yy = abs(self.parents[yy])
            if size_xx > size_yy:
                (xx, yy) = (yy, xx)
            self.parents[yy] += self.parents[xx]
            self.parents[xx] = yy

    def size(self, x):
        xx = self.find(x)
        return abs(self.parents[xx])

    def same(self, x, y):
        return 1 if self.find(x) == self.find(y) else 0

    def members(self, x):
        xx = self.find(x)
        return [i for i in range(self.n) if self.find(i) == xx]

    def roots(self):
        return [i for (i, x) in enumerate(self.parents) if x < 0]

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def state_grouping(self):
        return list(self.all_group_members().values())


uf = UnionFind(n)
for i in range(m):
    (a, b) = map(int, input().split())
    a -= 1
    b -= 1
    uf.union(a, b)
ans = 0
for i in range(n):
    ans += uf.same(i, P[i])
print(ans)
