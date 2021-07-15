class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
    
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)
        rx = self.rank[x]
        ry = self.rank[y]
        if px==py:
            return False
        if rx>ry:
            self.parent[py]=px
            self.rank[px]+=self.rank[py]
        else:
            self.parent[px]=py
            self.rank[py]+=self.rank[px]
        return True
                
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))
    
        edges.sort()
        res = 0
        ds = DSU(n)
        for cost, u, v in edges:
            if ds.union(u,v):
                res += cost
        return res
