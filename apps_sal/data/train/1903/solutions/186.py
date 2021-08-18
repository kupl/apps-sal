class Solution:
    def minCostConnectPoints(self, points: list(list())) -> int:
        n = len(points)
        if len(points) == 1:
            return 0
        res = 0
        curr = 0
        dis = [float('inf')] * n
        explored = set()

        for i in range(n - 1):
            x0, y0 = points[curr]
            explored.add(curr)
            for j, (x, y) in enumerate(points):
                if j in explored:
                    continue
                dis[j] = min(dis[j], abs(x - x0) + abs(y - y0))

            delta, curr = min((d, j) for j, d in enumerate(dis))
            dis[curr] = float('inf')
            res += delta

        return int(res)
