class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def dist(u, v):
            (x, y) = points[u]
            (x2, y2) = points[v]
            return abs(x - x2) + abs(y - y2)
        n = len(points)
        visited = [False] * n
        pq = [(0, 0)]
        ans = 0
        while pq:
            (cost, u) = heappop(pq)
            if visited[u]:
                continue
            visited[u] = True
            ans += cost
            for v in range(n):
                if visited[v]:
                    continue
                heappush(pq, (dist(u, v), v))
        return ans
