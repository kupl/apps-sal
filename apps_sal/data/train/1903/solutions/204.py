class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp == yp:
            return False
        if self.rank[xp] < self.rank[yp]:
            self.parent[xp] = yp
        elif self.rank[xp] > self.rank[yp]:
            self.parent[yp] = xp
        else:
            self.parent[xp] = yp
            self.rank[yp] += 1
        self.size -= 1
        return True
    def getSize(self):
        return self.size
    
class Solution:
    import heapq
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap, n = [], len(points)
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(heap, (dist, (i, j)))
        dsu = DSU(n + 1)
        res, i, j = 0, 0, 0
        while heap:
            dist, (i, j) = heapq.heappop(heap)
            if dsu.union(i, j):
                res += dist
                if dsu.getSize() == 2:
                    return res
        return 0
        

