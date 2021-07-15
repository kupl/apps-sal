class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dis = lambda x,y,x1,y1: abs(x-x1) + abs(y-y1)
        distances = []
        for i, (x, y) in enumerate(points):
            for j in range(i+1, len(points)):
                x1, y1 = points[j]
                d = dis(x, y, x1, y1)
                distances.append((d, i, j))
        uf = UnionFind(len(points))
        distances.sort()
        ans = 0
        for d, i, j in distances:
            if uf.union(i, j):
                ans += d
        return ans
        
class UnionFind:
    def __init__(self, n):
        self.component_count = n
        self.parents = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    # return true if two are newly unioned, false if already unioned.
    def union(self, x, y):
        x0 = self.find(x)
        y0 = self.find(y)
        if x0 == y0:
            return False
        if self.size[x0] < self.size[y0]:
            x0, y0 = y0, x0
        self.parents[y0] = x0
        self.size[x0] += self.size[y0]
        self.component_count -= 1
        return True
