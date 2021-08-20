class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        (n, curr, ans) = (len(points), 0, 0)
        if n == 1:
            return 0
        dist = [math.inf] * n
        visited = set()
        for i in range(n - 1):
            (x, y) = points[curr]
            visited.add(curr)
            for (j, (u, v)) in enumerate(points):
                if j in visited:
                    continue
                dist[j] = min(dist[j], abs(u - x) + abs(v - y))
            (delta, curr) = min(((d, j) for (j, d) in enumerate(dist)))
            dist[curr] = math.inf
            ans += delta
        return ans
