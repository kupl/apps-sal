class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        d = [[float('inf') for _ in range(n)] for _ in range(n)]

        for s, t, w in edges:
            d[s][t] = w
            d[t][s] = w

        for i in range(n):
            for s in range(n):
                for t in range(n):
                    d[s][t] = min(d[s][t], d[s][i] + d[i][t])

        neighbors = [0 for i in range(n)]
        for s in range(n):
            for t in range(n):
                if s != t and d[s][t] <= distanceThreshold:
                    neighbors[s] += 1

        min_value = float('inf')
        res = None

        for v in range(n):
            if neighbors[v] <= min_value:
                min_value = neighbors[v]
                res = v

        return res
