class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dis = [math.inf] * n
        visited = [False] * n
        ans = 0
        dis[0] = 0
        for i in range(0, n):
            (d, j) = min(((d, j) for (j, d) in enumerate(dis)))
            dis[j] = math.inf
            visited[j] = True
            ans += d
            for k in range(0, n):
                if j == k or visited[k]:
                    continue
                dis[k] = min(dis[k], abs(points[j][0] - points[k][0]) + abs(points[j][1] - points[k][1]))
        return ans
