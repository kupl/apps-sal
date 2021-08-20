class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        n = len(points)
        dist = [[0] * n for _ in range(n)]
        for i in range(n):
            (x1, y1) = points[i]
            for j in range(n):
                (x2, y2) = points[j]
                dist[i][j] = abs(x1 - x2) + abs(y1 - y2)
        origin = 0
        q = []
        for (j, d) in enumerate(dist[0]):
            heapq.heappush(q, (d, j))
        ans = 0
        visited = set([0])
        while len(visited) < n:
            (d, child) = heapq.heappop(q)
            if child not in visited:
                ans += d
                visited.add(child)
                for (j, n_d) in enumerate(dist[child]):
                    if j not in visited:
                        heapq.heappush(q, (n_d, j))
        return ans
