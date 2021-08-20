class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        for (u, v, w) in edges:
            dist[u][v] = w
            dist[v][u] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        mn = n + 1
        output = None
        for start in range(n):
            count = len([d for d in dist[start] if d <= distanceThreshold])
            if count <= mn:
                mn = count
                output = start
        return output
