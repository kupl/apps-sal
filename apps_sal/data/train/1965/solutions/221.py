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


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        '''
        for vertex
            if has type3 edge remove all other edges
            else:

        '''
        dsuA = DSU(n + 1)
        dsuB = DSU(n + 1)

        ans = 0
        for t, u, v in edges:
            if t == 3:
                if not dsuA.union(u, v):
                    ans += 1
                dsuB.union(u, v)
        for t, u, v in edges:
            if t == 1:
                if not dsuA.union(u, v):
                    ans += 1
            if t == 2:
                if not dsuB.union(u, v):
                    ans += 1
        return ans if dsuA.size(1) == dsuB.size(1) == n else -1
