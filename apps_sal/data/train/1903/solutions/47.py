import heapq

class DSU:
    def __init__(self, n):
        self.roots = [i for i in range(n)]
    def find(self, x):
        if self.roots[x] != x:
            self.roots[x] = self.find(self.roots[x])
        return self.roots[x]
    def union(self, x, y):
        self.roots[self.find(x)] = self.find(y)
        
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # minimum spanning tree
        
        n = len(points)
        if n == 1:
            return 0
        
        heap = []
        
        for i in range(n-1):
            for j in range(i+1, n):
                ax, ay = points[i]
                bx, by = points[j]
                heapq.heappush(heap, [abs(ax-bx) + abs(ay-by), i, j])
        #print(heap)
        count = 0
        dsu = DSU(n)
        while heapq:
            
            dist, i, j = heapq.heappop(heap)
            
            if dsu.find(i) != dsu.find(j):
                #print(dist, i, j)
                count += dist
                dsu.union(i, j)
            for i in range(n):
                dsu.find(i)
            if len(set(dsu.roots)) == 1:
                break
        
        return count
