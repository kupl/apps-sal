class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        n = len(points)
        g = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                x, y = points[i]
                xx, yy = points[j]
                g[i][j] = g[j][i] = abs(x - xx) + abs(y - yy)
        dist = [float('inf')] * n
        dist[0] = 0
        s = set(range(n))
        heap = [(0, 0)]
        while heap:
            d, u = heapq.heappop(heap)
            if u not in s:
                continue
            s.remove(u)
            for v in range(n):
                if v in s and g[u][v] < dist[v]:
                    dist[v] = g[u][v]
                    heapq.heappush(heap, (dist[v], v))
        return sum(dist)
