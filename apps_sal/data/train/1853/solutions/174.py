class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        for u in range(n):
            dist[u][u] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > (d := dist[i][k] + dist[k][j]):
                        dist[i][j] =  d
        neighbors = {len(list(filter(lambda x: 0 < x <= distanceThreshold, dist[i]))): i for i in range(n)}
        return neighbors[min(neighbors)]
