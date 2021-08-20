class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        uf = {}

        def find(x):
            uf.setdefault(x, x)
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            (px, py) = (find(x), find(y))
            if px != py:
                uf[px] = py

        @lru_cache(None)
        def dist(i, j):
            (x1, y1) = points[i]
            (x2, y2) = points[j]
            return abs(x1 - x2) + abs(y1 - y2)
        hp = []
        n = len(points)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                heapq.heappush(hp, (dist(i, j), i, j))
        while hp:
            (d, i, j) = heapq.heappop(hp)
            if find(i) != find(j):
                ans += d
                union(i, j)
        return ans
