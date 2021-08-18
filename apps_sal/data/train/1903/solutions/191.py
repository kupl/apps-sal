class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n_points = len(points)

        if n_points == 1:
            return 0

        res = 0
        curr = 0
        dist = [math.inf] * n_points
        explored = set()

        for i in range(n_points - 1):
            x0, y0 = points[curr]
            explored.add(curr)
            for j, (x, y) in enumerate(points):
                if j in explored:
                    continue

                dist[j] = min(dist[j], abs(x - x0) + abs(y - y0))

            delta, curr = min((d, j) for j, d in enumerate(dist))
            dist[curr] = math.inf
            res += delta

        return res
