class DSU:
    def __init__(self, N):
        self.par = list(range(N))
        self.rnk = [0] * N
        self.count = N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = list(map(self.find, (x, y)))
        if xr == yr:
            return False
        self.count -= 1
        if self.rnk[xr] < self.rnk[yr]:
            xr, yr = yr, xr
        if self.rnk[xr] == self.rnk[yr]:
            self.rnk[xr] += 1
        self.par[yr] = xr
        return True


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        uf_a, uf_b = DSU(n), DSU(n)

        ans = 0
        edges.sort(reverse=True)
        for t, u, v in edges:
            u, v = u - 1, v - 1
            if t == 3:
                ans += not (uf_a.union(u, v) and uf_b.union(u, v))
            elif t == 2:
                ans += not uf_b.union(u, v)
            else:
                ans += not uf_a.union(u, v)

        return ans if uf_a.count == 1 and uf_b.count == 1 else -1
