class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if len(points) == 1:
            return 0
        res = 0
        curr = 0
        dis = [math.inf] * n
        visited = set()
        for i in range(n - 1):
            (x0, y0) = points[curr]
            visited.add(curr)
            for (j, (x, y)) in enumerate(points):
                if j in visited:
                    continue
                dis[j] = min(dis[j], abs(x - x0) + abs(y - y0))
            (delta, curr) = (float('inf'), float('inf'))
            for (j, d) in enumerate(dis):
                (delta, curr) = min((delta, curr), (d, j))
            dis[curr] = math.inf
            res += delta
        return res
