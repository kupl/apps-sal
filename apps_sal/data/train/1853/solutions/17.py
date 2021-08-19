class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[math.inf] * n for _ in range(n)]
        for (i, j, w) in edges:
            dist[i][j] = w
            dist[j][i] = w
        for i in range(n):
            dist[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        res = []
        for i in range(n):
            res.append(sum((dist[i][j] <= distanceThreshold for j in range(n))))
        print(res)
        tmp = (n, 0)
        for (i, c) in enumerate(res):
            if (c, -i) < tmp:
                tmp = (c, -i)
        return -tmp[1]
