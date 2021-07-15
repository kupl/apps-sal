class DSU:
    def __init__(self, n):
        self.store = list(range(n))
        
    def find(self, idx):
        if idx != self.store[idx]:
            self.store[idx] = self.find(self.store[idx])
            
        return self.store[idx]
    
    def union(self, x, y):
        x_idx = self.find(x)
        y_idx = self.find(y)
        
        self.store[y_idx] = x_idx
        
        return x_idx != y_idx

        
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x0, y0 = points[i]
                x1, y1 = points[j]
                
                cost = abs(x0 - x1) + abs(y0 - y1)
                
                edges.append((cost, i, j))
                
        edges.sort(key=lambda x: x[0])
        
        res_cost = 0
        dsu = DSU(len(points))
        
        for weight, u, v in edges:
            if dsu.union(u, v):
                res_cost += weight
        
        return res_cost
                
                

