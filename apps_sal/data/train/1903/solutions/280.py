class DisjointSet:
    def __init__(self, n):
        self.rank = {i:i for i in range(n)}
        self.size = n
        self.parent = {i:i for i in range(n)}
        
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        root_i, root_j = self.find(i), self.find(j)
        if root_i == root_j:
            return False
        
        if self.rank[root_i] > self.rank[root_j]:
            self.parent[root_j] = root_i
        elif self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        else:
            self.parent[root_j] = root_i
            self.rank[root_i] += 1
        self.size -= 1
        return True
        

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        ds = DisjointSet(n)
        
        d = []
        for i in range(n):
            for j in range(i, n):
                d_ij = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                heapq.heappush(d, [d_ij, i, j])
        
        min_cost = 0
        while ds.size > 1:
            d_ij, i, j = heapq.heappop(d)
            if ds.union(i, j):
                min_cost += d_ij
        return min_cost

