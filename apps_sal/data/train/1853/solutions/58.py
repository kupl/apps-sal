class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distance = [[float('inf') for _ in range(n)] for _ in range(n)]

        for i, j, w in edges:
            distance[i][j] = w
            distance[j][i] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

        m = collections.defaultdict()
        ans = 0

        print(distance)

        for i in range(n):
            temp = 0
            for j in range(n):
                if distance[i][j] <= distanceThreshold and i != j:
                    temp += 1
            m[temp] = i
        print(m)
        return m[min(m.keys())]
