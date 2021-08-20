class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0
        res = 0
        curr = 0
        dis = [float('inf')] * n
        explored = set()
        for i in range(n - 1):
            (point_x, point_y) = points[curr]
            explored.add(curr)
            for (j, (x, y)) in enumerate(points):
                if j in explored:
                    continue
                dis[j] = min(dis[j], abs(x - point_x) + abs(y - point_y))
            (delta, curr) = min(((d, j) for (j, d) in enumerate(dis)))
            dis[curr] = float('inf')
            res += delta
        return res
