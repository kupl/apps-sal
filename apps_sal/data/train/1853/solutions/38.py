class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        matrix = [[float('inf') for x in range(n)] for y in range(n)]

        # populate self loops
        for i in range(n):
            matrix[i][i] = 0

        # populate initial matrix
        for u, v, w in edges:
            matrix[u][v] = w
            matrix[v][u] = w

        # floyd-warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

        # get amount of below threshold cities
        res = Counter()
        for i, row in enumerate(matrix):
            for j, dist in enumerate(row):
                if dist <= distanceThreshold and i != j:
                    res[i] += 1

        best = 0
        for i in range(n):
            if res[i] <= res[best]:
                best = i
        return best

        # check if unconnected cities
        unconnected = []
        i = 0
        while i < n:
            if res[i] == 0:
                # not conencted
                unconnected.append(i)
            i += 1

        if len(unconnected) == 1:
            return unconnected[0]
        elif len(unconnected) > 1:
            return max(unconnected)

        # all cities are connected with each other, get min value
        ans = min(res.values())
        max_city = 0

        # if multiple cities with same minimum neighbours, select biggest one
        for city in range(len(res)):
            if res[city] <= ans and city > max_city:
                max_city = city

        return max_city
