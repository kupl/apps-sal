class UF:
    def __init__(self, n):
        self.parents = [i for i in range(n)]

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        self.parents[py] = px
        return True
        
        
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distances = []
        for i, [xi, yi] in enumerate(points):
            for j in range(i + 1, len(points)):
                xj, yj = points[j]
                d = abs(xi - xj) + abs(yi - yj)
                distances.append([d, i, j])
        
        distances.sort()
        uf = UF(len(points))
        ans = 0
        for d, i, j in distances:
            if uf.union(i, j):
                ans += d
        
        return ans
