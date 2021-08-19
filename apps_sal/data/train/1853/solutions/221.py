class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dis = [[float('inf')] * n for _ in range(n)]
        for (i, j, w) in edges:
            dis[i][j] = w
            dis[j][i] = w
        for i in range(0, n):
            dis[i][i] = 0
        for k in range(0, n):
            for i in range(0, n):
                for j in range(0, n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        nbs = [0] * n
        for i in range(0, n):
            nbs[n - 1 - i] = len([j for j in dis[i] if 0 < j <= distanceThreshold])
        return n - 1 - nbs.index(min(nbs))
