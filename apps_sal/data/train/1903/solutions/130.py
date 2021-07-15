class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        res = 0
        dis = [float('inf')] * len(points)
        visited = set()
        cur = 0
        for i in range(len(points) - 1):
            visited.add(cur)
            for j in range(len(points)):
                if j not in visited:
                    dis[j] = min(dis[j], dist(points[cur], points[j]))
            d, cur = min((d, j) for j, d in enumerate(dis))
            dis[cur] = float('inf')
            res += d
        return res
