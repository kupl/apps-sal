class UnionFind:
    def __init__(self,size):
        self.size = size
        self.components = size
        self.parent = [0] * size
        self.sizeArray = [0] * size
        for i in range(size):
            self.parent[i] = i
            self.sizeArray[i] = 1
        
    def find(self,a):
        while a != self.parent[a]:
            a = self.parent[a]    
        return a
    
    def unify(self, a, b):
        p_a = self.find(a)
        p_b = self.find(b)
        if p_a == p_b:
            return
        if self.sizeArray[p_a] < self.sizeArray[p_b]:
            self.sizeArray[p_b] += self.sizeArray[p_a]
            self.parent[p_a] = p_b
        else:
            self.sizeArray[p_a] += self.sizeArray[p_b]
            self.parent[p_b] = p_a
        
        self.components -= 1
        
    def num_components(self):
        return self.components
    
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        
        _map = {}
        k = 0
        for p in points:
            _map[(p[0], p[1])] = k
            k += 1
        
        for i in range(n):
            for j in range(i + 1, n):
                u = points[i]
                v = points[j]
                dist = abs(u[0] - v[0]) + abs(u[1] - v[1])
                edges.append((u, v, dist))
                
        edges.sort(key=lambda x:x[2])
        #print(edges)
        
        ds = UnionFind(n)
        
        min_cost = 0
        
        for edge in edges:
            u = _map[(edge[0][0], edge[0][1])]
            v = _map[(edge[1][0], edge[1][1])]
            d = edge[2]
            
            if ds.find(u) != ds.find(v):
                ds.unify(u, v)
                min_cost += d
        
        return min_cost
