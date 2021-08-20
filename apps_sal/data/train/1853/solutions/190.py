class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dis = [[float('inf')] * n for _ in range(n)]
        for (u, v, w) in edges:
            dis[u][v] = dis[v][u] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i != j and dis[i][j] > dis[i][k] + dis[k][j]:
                        dis[i][j] = dis[i][k] + dis[k][j]
        d = {i: len([dis[i][j] for j in range(n) if dis[i][j] <= distanceThreshold]) for i in range(n)}
        minv = float('inf')
        res = -1
        for i in reversed(range(n)):
            if d[i] < minv:
                res = i
                minv = d[i]
        return res
