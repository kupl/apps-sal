class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for pair in edges:
            a, b, c = pair
            dist[a][b] = dist[b][a] = c
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        res = {len([x for x in dist[i] if x <= distanceThreshold]): i for i in range(n)}
        return res[min(res)]
