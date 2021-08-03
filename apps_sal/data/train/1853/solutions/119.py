class Solution:
    def findTheCity(self, n, edges, maxd):
        dis = [[float('inf')] * n for _ in range(n)]
        for i, j, w in edges:
            dis[i][j] = dis[j][i] = w
        for i in range(n):
            dis[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

        temp = [sum(d <= maxd for d in dis[i]) for i in range(n)]
        return [i for i, x in enumerate(temp) if x == min(temp)][-1]
