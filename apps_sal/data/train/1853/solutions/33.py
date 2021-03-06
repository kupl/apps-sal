class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dis = [[float('inf') for _ in range(n)] for _ in range(n)]
        for (i, j, w) in edges:
            dis[i][j] = dis[j][i] = w
        for i in range(n):
            dis[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        res = {}
        for i in range(n):
            count = 0
            for d in dis[i]:
                if d <= distanceThreshold:
                    count += 1
            res[count] = i
        return res[min(res)]
