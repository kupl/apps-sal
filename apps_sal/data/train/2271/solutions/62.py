import sys
input = sys.stdin.readline


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

    def size(self, x):
        return -self.parents[self.find(x)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for (i, x) in enumerate(self.parents) if x < 0]

    def all_group_members(self):
        d = {root: [] for root in self.roots()}
        for i in range(self.n):
            d[self.find(i)].append(i)
        return d

    def __str__(self):
        return '\n'.join(('{}: {}'.format(r, self.members(r)) for r in self.roots()))


(N, M) = list(map(int, input().split()))
p = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(M)]
uf = UnionFind(N)
for (x, y) in xy:
    x -= 1
    y -= 1
    uf.union(x, y)
ans = 0
for renketu_seibun in list(uf.all_group_members().values()):
    can_reach = set([p[v] - 1 for v in renketu_seibun])
    for v in renketu_seibun:
        ans += v in can_reach
print(ans)
