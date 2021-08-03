from collections import defaultdict


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dmatrix = [[9999999999999999 for _ in range(n)] for _ in range(n)]

        for a, b, w in edges:
            dmatrix[a][b] = w
            dmatrix[b][a] = w

        for source in range(n):
            dmatrix[source][source] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dmatrix[i][j] > dmatrix[i][k] + dmatrix[k][j]:
                        dmatrix[i][j] = dmatrix[i][k] + dmatrix[k][j]

        cities = [(sum([dist <= distanceThreshold for dist in dmatrix[city]]), -city) for city in range(n)]
        _, best_city = list(sorted(cities))[0]
        return -best_city
