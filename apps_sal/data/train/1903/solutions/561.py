class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if len(points) == 1:
            return 0
        res = 0
        curr = 0
        dis = [math.inf] * n
        explored = set()

        for _ in range(n - 1):
            x0, y0 = points[curr]
            explored.add(curr)
            dis[curr] = math.inf
            for j, (x, y) in enumerate(points):
                if j in explored:
                    continue
                if dis[j] > abs(x - x0) + abs(y - y0):
                    dis[j] = abs(x - x0) + abs(y - y0)

            delta, curr = min((d, j) for j, d in enumerate(dis))
            res += delta

        return res
