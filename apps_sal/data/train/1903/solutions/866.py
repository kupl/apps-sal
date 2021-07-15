class DSU:
    def __init__(self, N):
        self.p = [i for i in range(N)]
        
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        self.p[py] = px
        
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        heap = []
        result = 0
        
        n = len(points)
        
        for i in range(n-1):
            for j in range(i+1, n):
                heapq.heappush(heap, (abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1]), i, j))

        dsu = DSU(n)
        
        while heap:
            d, i, j = heapq.heappop(heap)
            pi = dsu.find(i)
            pj = dsu.find(j)
            
            if pi != pj:
                result += d
                dsu.union(i, j)
        
        return result

