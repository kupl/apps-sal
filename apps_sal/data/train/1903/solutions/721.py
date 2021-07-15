class Graph:
    def __init__(self, v =0):
        self.v = v
        self.edge = []
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n
        
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, u, v):
        uroot, vroot = self.find(u), self.find(v)
        if uroot == vroot:
            return False
        elif self.rank[uroot] < self.rank[vroot]:
            self.parent[uroot] = vroot
            self.rank[vroot] += 1
        else:
            self.parent[vroot] = uroot
            self.rank[uroot] += 1
        return True
    
class Solution:
    def distance(self, point1: List[int], point2: List[int]):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points or len(points)<2:
            return 0
        n = len(points)
        graph = Graph(n)
        tot = 0
        for i in range(n):
            for j in range(i+1, n):
                d = self.distance(points[i], points[j])
                graph.edge.append([i,j,d])

        graph.edge = sorted(graph.edge, key=lambda item: item[2])
        
        uf = UnionFind(n)
        for u,v,w in graph.edge:
            if uf.union(u,v):
                tot += w
        return tot

