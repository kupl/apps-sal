class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
    
    def find(self, u):
        orig = u
        while u != self.parents[u]:
            u = self.parents[u]
        
        self.parents[orig] = u
        return u
    
    def union(self, u, v):
        u,v = sorted([self.find(u),self.find(v)])
        
        if u!=v:
            self.parents[v] = u
            return True
        return False
    
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        distances = {}
        
        def compute(p1,p2):
            x1,y1 = p1
            x2,y2 = p2
            return abs(x1-x2)+abs(y1-y2)
        
        for i,p1 in enumerate(points):
            for j in range(i+1,len(points)):
                p2 = points[j]
                
                distances[(i,j)] = compute(p1,p2)
        
        dsu = DSU(len(points))
        
        res = 0
        for (u,v),d in sorted(list(distances.items()), key=lambda x: x[1]):
            if dsu.union(u,v):
                res+=d
        return res

