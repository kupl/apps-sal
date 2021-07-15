import heapq

class UnionFind:
    \"\"\"
    Class that implements the union-find structure with
    union by rank and find with path compression
    \"\"\"
     
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0 for x in range(n)]
 
    def find(self, v):
        if not v == self.parent[v]:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
 
    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return
        if self.rank[xRoot] > self.rank[yRoot]:
            self.parent[yRoot] = xRoot
        else:
            self.parent[xRoot] = yRoot
            if self.rank[xRoot] == self.rank[yRoot]:
                self.rank[yRoot] += 1
                
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        mat = [[0] * len(points) for _ in range(len(points))]
        heap = []
        union_find = UnionFind(len(points))
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                mat[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(heap, (mat[i][j], i, j))
        
        total_cost = 0
        while heap:
            dist, a, b = heapq.heappop(heap)
            
            # if a, b not in same group:
            if union_find.find(a) != union_find.find(b):
                union_find.union(a, b)
                total_cost += dist
            
        return total_cost
