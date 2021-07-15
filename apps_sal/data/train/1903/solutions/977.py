class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        
    def find(self, a):
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a
    
    def isConnected(self, a, b):
        return self.find(a) == self.find(b)
    
    def union(self, a, b):
        parentA = self.find(a)
        parentB = self.find(b)
        if self.isConnected(a, b): 
            return
        if self.size[parentA] > self.size[parentB]:
            self.parent[parentB] = parentA
            self.size[parentA] += self.size[parentB]
        else:
            self.parent[parentA] = parentB
            self.size[parentB] += self.size[parentA]
        
        
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                manhattanDist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((manhattanDist, i ,j))
        edges.sort()
        res = 0
        uf = UF(n)
        for cost, i, j in edges:
            if not uf.isConnected(i, j):
                uf.union(i, j)
                res += cost
        return res

