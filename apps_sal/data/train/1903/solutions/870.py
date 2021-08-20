class Solution:

    class UnionFinder:

        def __init__(self, n):
            self.parents = list(range(n))
            self.ranks = [0] * n

        def find(self, x):
            if self.parents[x] != x:
                self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

        def join(self, x, y):
            p1 = self.find(x)
            p2 = self.find(y)
            if p1 == p2:
                return False
            r1 = self.ranks[p1]
            r2 = self.ranks[p2]
            if r1 < r2:
                self.parents[p1] = p2
            elif r2 < r1:
                self.parents[p2] = p1
            else:
                self.parents[p1] = p2
                self.ranks[p2] += 1
            return True

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = list()
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                heapq.heappush(heap, (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))
        union_finder = Solution.UnionFinder(len(points))
        ans = 0
        while heap:
            (d, i, j) = heapq.heappop(heap)
            if union_finder.join(i, j):
                ans += d
        return ans
