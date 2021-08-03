class Solution:
    def findTheCity(self, N: int, edges: List[List[int]], distanceThreshold: int) -> int:

        dist = [[float('inf')] * N for _ in range(N)]

        for u in range(N):
            dist[u][u] = 0

        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        # Floyd
        for k in range(N):
            for j in range(N):
                for i in range(N):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        # Calculate
        min_cities = float('inf')
        ret = None
        print(dist)

        for u in range(N):
            reach = 0
            for v in range(N):
                if u != v and dist[u][v] <= distanceThreshold:
                    reach += 1

            if reach <= min_cities:
                min_cities = reach
                ret = u

        return ret
