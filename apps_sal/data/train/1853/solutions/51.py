class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        import numpy
        adj = [[float('inf')] * n for _ in range(n)]

        for u, v, w in edges:
            adj[u][v] = adj[v][u] = w

        for i in range(n):
            adj[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])
        print(numpy.matrix(adj))

        res = {sum(d <= distanceThreshold for d in adj[i]): i for i in range(n)}
        print(res)
        return res[min(res)]
