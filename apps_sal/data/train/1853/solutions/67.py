class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dis = [[float(\"inf\") ] * n for _ in range(n)]
        for i in range(n):
            dis[i][i] = 0
        for u, v, w in edges:
            dis[u][v] = dis[v][u] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        res = -1
        min_count = float(\"inf\")
        for k in range(n-1, -1, -1):
            count = 0
            for j in range(n):
                if dis[k][j] <= distanceThreshold:
                    count += 1
            if min_count > count:
                res = k
                min_count = count
        return res
