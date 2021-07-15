        
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        
        p1, p2 = self.find(u), self.find(v)
        
        if p1 == p2:
            return False
        
        self.parent[p1] = p2
        return True
    

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0
        
        n = len(points)
        edges = []
        
        for i in range(n-1):
            for j in range(i+1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))
        
        edges.sort()
        
        res = 0
        uf = UnionFind(n)
        
        for cost, u, v in edges:
            if uf.union(u, v):
                res += cost
        return res
        
        

