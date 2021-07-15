class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        hp, uf = [], UF(len(points))
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1, p2 = points[i], points[j]
                weight = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                heapq.heappush(hp, (weight, i, j))
        res = 0
        while hp:
            weight, a, b = heapq.heappop(hp)
            if uf.find(a) != uf.find(b):
                uf.union(a, b)
                res += weight
        return res
    
class UF:
    def __init__(self, n):
        self.uf = list(range(n))
        self.sz = [1] * n
        self.root_cnt = n
    
    def find(self, c):
        root = c
        while root != self.uf[root]:
            root = self.uf[root]
        while self.uf[c] != root:
            p = self.uf[c]
            self.uf[c] = root
            c = p
        return root
    
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb: return False
        if self.sz[ra] < self.sz[rb]:
            self.uf[ra] = rb
            self.sz[rb] += self.sz[ra]
        else:
            self.uf[rb] = ra
            self.sz[ra] += self.sz[rb]
        self.root_cnt -= 1
        return True
