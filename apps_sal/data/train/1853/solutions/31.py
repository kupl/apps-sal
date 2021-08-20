class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = [[float('inf')] * n for i in range(n)]
        for i in range(n):
            adj[i][i] = 0
        for (u, v, w) in edges:
            adj[u][v] = w
            adj[v][u] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])
        print(adj)
        res = float('inf')
        res_city = -1
        for i in range(n):
            count = 0
            for j in range(n):
                if i != j:
                    if adj[i][j] <= distanceThreshold:
                        count += 1
            if count <= res:
                res = count
                res_city = i
        return res_city
