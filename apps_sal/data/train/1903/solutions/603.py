class DSU:
    def __init__(self, n):
        self.par = [i for i in range(n)]
    
    def find(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        self.par[px] = py
        return

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(x, y):
            return abs(x[0]-y[0]) + abs(x[1]-y[1])
        
        cnt = 0
        n = len(points)
        needs = n-1
        dsu = DSU(n)
        
        dists = [(dist(points[i], points[j]), i, j) for i in range(n) for j in range(n) if i != j]
        dists.sort()
        
        i = 0
        while i < len(dists) and needs:
            d, x, y = dists[i]
            px, py = dsu.find(x), dsu.find(y)
            if px == py:
                i += 1
            else:
                # print(points[x], points[y])
                cnt += d
                dsu.union(x, y)
                needs -= 1
        return cnt
        

