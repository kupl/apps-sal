import sys
readline = sys.stdin.readline

class UnionFind(object):
    def __init__(self, n):
        self._par = list(range(n))
        self.size = [1]*n

    def root(self, v):
        if self._par[v] == v:
            return v
        self._par[v] = self.root(self._par[v])
        return self._par[v]
    
    def unite(self, u, v):
        u, v = self.root(u), self.root(v)
        if u==v:
            return False
        if self.size[u] > self.size[v]:
            u, v = v, u
        self.size[v] += self.size[u]
        self._par[u] = v

    def is_connected(self, u, v):
        return self.root(u)==self.root(v)

n, m = map(int, readline().split())
P = list(map(lambda x:int(x)-1, readline().split()))
uf = UnionFind(n)
for _ in range(m):
    x, y = map(lambda x:int(x)-1, readline().split())
    uf.unite(x,y)

ans = 0
for i in range(n):
    if uf.is_connected(i, P[i]):
        ans += 1
print(ans)
