class UnionFind:
    def __init__(self, size):
        self._parent = list(range(size))
        self._size = [1] * size
    
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self._size[a] < self._size[b]:
            a, b = b, a
        self._parent[b] = a
        self._size[a] += self._size[b]
        return True
    
    def find(self, x):
        while self._parent[x] != x:
            self._parent[x] = self._parent[self._parent[x]]
            x = self._parent[x]
        return x
    
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        edges = []
        for u in range(n):
            x0, y0 = points[u]
            for v in range(u + 1, n):
                x1, y1 = points[v]
                edges.append((u, v, abs(x0 - x1) + abs(y0 - y1)))
        edges.sort(key=lambda e: e[2])
        
        uf = UnionFind(n)
        cost = 0
        
        for u, v, w in edges:
            if uf.union(u, v):
                cost += w
        
        return cost
