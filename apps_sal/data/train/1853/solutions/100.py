class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[float('inf')] * n for i in range(n)]
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i == j:
                        graph[i][j] = 0
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        minCount, city = float('inf'), -1
        for i in range(n):
            count = sum([1 for j in range(n) if j != i and graph[i][j] <= distanceThreshold])
            if count <= minCount:
                minCount, city = count, i
        return city
