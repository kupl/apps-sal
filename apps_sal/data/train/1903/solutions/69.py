class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        d = {}
        min_heap = []
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i][0], points[i][1]
                x2, y2 = points[j][0], points[j][1]
                dist = abs(x1 - x2) + abs(y1 - y2)
                d[(x1, y1)] = (x1, y1)
                d[(x2, y2)] = (x2, y2)
                heapq.heappush(min_heap, (dist, (x1, y1), (x2, y2)))

        def find(x):
            px = d[x]
            if px != x:
                d[x] = find(px)
            return d[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                d[px] = py

        min_cost = 0
        while min_heap:
            c, p1, p2 = heapq.heappop(min_heap)
            pa1, pa2 = find(p1), find(p2)
            if pa1 != pa2:
                union(p1, p2)
                min_cost += c
        return min_cost
