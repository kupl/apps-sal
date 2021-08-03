class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.height = [0 for i in range(n)]

    def find(self, x):
        if self.parent[x] == x:
            return x
        result = self.find(self.parent[x])
        self.parent[x] = result
        return result

    def merge(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if self.height[rx] > self.height[ry]:
            self.parent[ry] = rx
        elif self.height[rx] < self.height[ry]:
            self.parent[rx] = ry
        else:
            self.parent[rx] = ry
            self.height[rx] += 1


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                heappush(edges, (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))
        uf = UnionFind(n)
        ans = 0
        while edges:
            cost, va, vb = heappop(edges)
            if uf.find(va) == uf.find(vb):
                pass
            else:
                uf.merge(va, vb)
                ans += cost
        return ans
