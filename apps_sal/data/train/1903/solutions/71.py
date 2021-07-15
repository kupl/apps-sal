class DSU:
    
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n
        
    def find(self, x):
        p = self.parents[x]
        if p == x: return x
        self.parents[x] = self.find(p)
        return self.parents[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False
        sx, sy = self.sizes[px], self.sizes[py]
        if sy > sx: px, py = py, px
        self.parents[py] = px
        self.sizes[px] = sx + sy
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i1, p1 in enumerate(points):
            for i2 in range(i1+1, len(points)):
                p2 = points[i2]
                d = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                edges.append([d, i1, i2])
                
        edges.sort()
        
        dsu = DSU(len(points))
        
        t = 0
        for c, i1, i2 in edges:
            if dsu.union(i1, i2):
                t += c
                
        return t
            

