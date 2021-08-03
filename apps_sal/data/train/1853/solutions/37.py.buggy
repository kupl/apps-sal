class Solution:
    def findTheCity(self, n, edges, maxd):
        \"\"\"
        * dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        # res = {sum(d <= maxd for d in dis[i]): i for i in range(n)}
        \"\"\"
        dis = [[float('inf')] * n for _ in range(n)]
        for i, j, w in edges:
            dis[i][j] = dis[j][i] = w
        for i in range(n):
            dis[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        res = {sum(d <= maxd for d in dis[i]): i for i in range(n)}
        return res[min(res)]

