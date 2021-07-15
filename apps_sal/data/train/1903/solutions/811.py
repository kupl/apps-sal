class DSU:
    def __init__(self, n):
        self.par = list(range(n))
        self.rnk = [0] * n

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.rnk[xr] < self.rnk[yr]:
            xr, yr = yr, xr
        if self.rnk[xr] == self.rnk[yr]:
            self.rnk[xr] += 1
        self.par[yr] = xr
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        edges = []
        for u in range(N-1):
            for v in range(u+1, N):
                edges.append([u, v, abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])])
                
        def MST():
            # Kruskals, edges sorted
            dsu = DSU(N)
            ans = 0
            for u, v, w in sorted(edges, key=lambda e: e[2]):
                if dsu.union(u, v):
                    ans += w
            return ans
        
        return MST()

