class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
            
                dist = abs(x1-x2) + abs(y1-y2)
                heap.append((dist, i, j))
        
        heapify(heap)
        uf = UnionFind(len(points))
        res = 0
        
        while heap:
            dist, x, y = heappop(heap)
            if uf.union(x, y):
                res += dist
                
        return res
    
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
        
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        
        else:
            self.parent[root_x] = root_y
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_y] += 1
        
        return True
    
    def find(self, x):
        while x != self.parent[x]:
            # self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
                
        
        
        
        

