class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = []
        for i in range(n):
            graph.append([float('inf')] * n)
        for i in range(n):
            graph[i][i] = 0
        for [edge1, edge2, weight] in edges:
            graph[edge1][edge2] = weight
            graph[edge2][edge1] = weight
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        minNode = -1
        minCount = 101
        for i in range(n):
            count = 0
            for j in range(n):
                if graph[i][j] <= distanceThreshold:
                    count += 1
            if count <= minCount:
                minCount = count
                minNode = i
        return minNode
