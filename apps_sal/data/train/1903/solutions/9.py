class DSU:
    def __init__(self, N):
        self.par = list(range(N))
        self.sz = [1]*N
        
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
        return True
    
    def size(self, x):
        return self.sz[self.find(x)]
    
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        edges = []
        N = len(points)
        for i in range(N):
            for j in range(i+1,N):
                d = abs(points[i][0]-points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append([d, i, j])
                
        edges.sort()
        
        u = DSU(N)
        res = 0
        
        for edge in edges:
            if u.union(edge[1], edge[2]):
                res += edge[0]
                
        return res
