import sys


class Solution:

    def constructGraph(self, edges, n):
        graph = [[sys.maxsize for i in range(n)] for j in range(n)]
        for (i, j, k) in edges:
            graph[i][j] = k
            graph[j][i] = k
        return graph

    def floydWarshall(self, graph, n):
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i == j:
                        graph[i][j] = 0
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                    graph[j][i] = graph[i][j]

    def getCitiesUnderThreshold(self, graph, distanceThreshold, n):
        arr = [None for i in range(n)]
        for i in range(n):
            lis = []
            for j in range(n):
                if graph[i][j] <= distanceThreshold and graph[i][j] != 0:
                    lis.append(j)
            arr[i] = lis
        return arr

    def cityWithLeastNumber(self, arr):
        minNum = sys.maxsize
        for (i, j) in enumerate(arr):
            if len(j) <= minNum:
                minNum = len(j)
                curr = i
        return curr

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = self.constructGraph(edges, n)
        self.floydWarshall(graph, n)
        arr = self.getCitiesUnderThreshold(graph, distanceThreshold, n)
        curr = self.cityWithLeastNumber(arr)
        return curr
