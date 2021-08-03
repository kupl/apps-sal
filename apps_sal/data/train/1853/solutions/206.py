class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        MAX_VAL = 1e6 + 1
        self.graph = [[MAX_VAL for _ in range(n)] for _ in range(n)]
        for idx in range(n):
            self.graph[idx][idx] = 0
        for edge in edges:
            self.graph[edge[0]][edge[1]] = edge[2]
            self.graph[edge[1]][edge[0]] = edge[2]
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if self.graph[i][k] + self.graph[k][j] < self.graph[i][j]:
                        self.graph[i][j] = self.graph[i][k] + self.graph[k][j]
        results = []
        for idx in range(n):
            results.append((idx, len([_ for _ in range(n) if self.graph[idx][_] <= distanceThreshold])))
        return sorted(results, key=lambda x: (x[1], -x[0]))[0][0]
