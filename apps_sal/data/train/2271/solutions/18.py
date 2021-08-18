import sys


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def root(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def merge(self, x, y):
        x, y = self.root(x), self.root(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.size[x] += self.size[y]
        self.parent[y] = x
        return True

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def getsize(self, x):
        return self.size[self.root(x)]


readline = sys.stdin.readline
read = sys.stdin.read

n, m = list(map(int, readline().split()))
*p, = list(map(int, readline().split()))

UF = UnionFind(n)
for _ in range(m):
    x, y = list(map(int, readline().split()))
    UF.merge(x - 1, y - 1)

q = [set() for _ in range(n)]
r = [set() for _ in range(n)]

for i in range(n):
    v = UF.root(i)
    q[v].add(i)
    r[v].add(p[i] - 1)

ans = 0
for i in range(n):
    ans += len(q[i] & r[i])

print(ans)
