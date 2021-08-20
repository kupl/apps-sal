class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0
        ds = UFind(n)
        hp = []
        heapq.heapify(hp)
        for i in range(n - 1):
            for j in range(i + 1, n):
                mhd = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(hp, (mhd, i, j))
        ans = 0
        while ds.count > 1:
            (mhd, i, j) = heapq.heappop(hp)
            if ds.union(i, j):
                ans += mhd
        return ans


class UFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        (x_par, y_par) = (self.find(x), self.find(y))
        if x_par == y_par:
            return False
        else:
            self.count -= 1
            if self.rank[x_par] < self.rank[y_par]:
                self.parent[x_par] = y_par
            elif self.rank[x_par] > self.rank[y_par]:
                self.parent[y_par] = x_par
            else:
                self.parent[x_par] = y_par
                self.rank[y_par] += 1
            return True
