class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], dist: int) -> int:
        if n == 2:
            return 1

        graph = [[float('inf')] * n for _ in range(n)]
        for s, e, w in edges:
            graph[s][e] = w
            graph[e][s] = w

        for i in range(n):
            graph[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if graph[i][j] > (d := graph[i][k] + graph[k][j]):
                        graph[i][j] = d

        nei = {len(list(filter(lambda x: 0 < x <= dist, graph[i]))): i for i in range(n)}
        return nei[min(nei)]
