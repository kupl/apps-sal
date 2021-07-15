class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        dis = [math.inf] * n
        curr = 0
        explored = set()
        for _ in range(n - 1):
            x0, y0 = points[curr]
            explored.add(curr)
            for i, (x, y) in enumerate(points):
                if i in explored : continue
                dis[i] = min(dis[i], abs(x - x0) + abs(y - y0))
            delta, curr = min( (d, idx) for idx, d in enumerate(dis))
            res += delta
            dis[curr] = math.inf
        return res

