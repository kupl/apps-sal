class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # matrices
        # for i,j,k
        # min value
        matrix = [[float('inf') for x in range(n)] for y in range(n)]

        # build initial matrix
        for i in range(n):
            matrix[i][i] = 0

        for u, v, w in edges:
            matrix[u][v] = w
            matrix[v][u] = w

        print(matrix)

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

        print(matrix)
        res = defaultdict(int)
        for i, row in enumerate(matrix):
            for j, dist in enumerate(row):
                if dist <= distanceThreshold and i != j:
                    res[i] += 1

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

        ans = min(res.values())
        max_city = 0

        for city in range(len(res)):
            if res[city] <= ans and city > max_city:
                max_city = city

        print(res)
        print(ans)
        print(max_city)
        return max_city
