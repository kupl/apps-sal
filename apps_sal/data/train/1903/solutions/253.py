import heapq


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        fathers = list(range(n))
        queue = []
        for (i, p1) in enumerate(points):
            for j in range(i + 1, n):
                p2 = points[j]
                d = self.distance(p1, p2)
                heapq.heappush(queue, (d, i * n + j, i, j))

        def find(fathers, v):
            if fathers[v] != v:
                fathers[v] = find(fathers, fathers[v])
            return fathers[v]

        def union(fathers, a, b):
            rootA = find(fathers, a)
            rootB = find(fathers, b)
            if rootA != rootB:
                fathers[rootB] = rootA
        cnt = 0
        edges = 0
        while queue and edges < n - 1:
            (d, _, i, j) = heapq.heappop(queue)
            rootI = find(fathers, i)
            rootJ = find(fathers, j)
            if rootI != rootJ:
                cnt += d
                edges += 1
                union(fathers, rootI, rootJ)
        return cnt

    def distance(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
