import math

class DSU:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
    
    def find(self, x):
        while self.parent[x] != x:
            x_p = self.parent[x]
            self.parent[x] = self.parent[x_p]  # path compression
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        x_p = self.find(x)
        y_p = self.find(y)
        if x_p != y_p:   # not in the same joint set
            self.parent[x_p] = y_p    # parent of y is the new root


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points)):
            for j in range(len(points)):
                dist = self.distance(points[i], points[j])
                edges.append((dist, i, j))
        edges = sorted(edges, key=lambda x:x[0])
        
        ans = 0
        n = len(points)
        dsu = DSU(n)
        i = 0
        j = 0 # inter through the edges
        while i < n-1:  # MST algo.
            dist, a, b = edges[j]
            a_p = dsu.find(a)
            b_p = dsu.find(b)
            if a_p != b_p:
                dsu.union(a, b)
                i += 1
                ans += dist
            j += 1
        return ans
                
    def distance(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
