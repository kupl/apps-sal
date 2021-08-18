class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        minDistance = collections.defaultdict(lambda: collections.defaultdict(lambda: math.inf))
        for i in range(n):
            minDistance[i][i] = 0

        for u, v, weight in edges:
            minDistance[u][v] = weight
            minDistance[v][u] = weight

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    minDistance[i][j] = min(minDistance[i][j], minDistance[i][k] + minDistance[k][j])

        minNeighborCount = math.inf
        minCity = -1

        for i in range(n):
            neighborCount = sum(minDistance[i][j] <= distanceThreshold for j in range(n) if j != i)

            if neighborCount <= minNeighborCount:
                minNeighborCount = neighborCount
                minCity = i

        return minCity
