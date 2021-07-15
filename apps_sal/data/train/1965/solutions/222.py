class DSU:
    def __init__(self, N):
        self.par = list(range(N))
        self.sz = [1] * N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.sz[xr] < self.sz[yr]:
            xr, yr = yr, xr
        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]
        self.sz[yr] = self.sz[xr]
        return True

    def size(self, x):
        return self.sz[self.find(x)]

class Solution(object):
    def maxNumEdgesToRemove(self, N, edges):
        for row in edges:
            # row[0] -= 1
            row[1] -= 1
            row[2] -= 1
        alice = []
        bob = []
        both = []
        
        for t, u, v in edges:
            if t == 1:
                alice.append([u,v])
            elif t==2:
                bob.append([u,v])
            else:
                both.append([u,v])
        dsu1 = DSU(N)
        dsu2 = DSU(N)
        ans = 0
        for u,v  in both:
            dsu2.union(u,v)
            if not dsu1.union(u, v):
                ans += 1
        for u,v  in alice:
            if not dsu1.union(u,v): ans += 1
        for u,v in bob:
            if not dsu2.union(u,v): ans += 1
        
        if dsu1.size(0) != N:
            return -1
        if dsu2.size(0) != N:
            return -1
        return ans

