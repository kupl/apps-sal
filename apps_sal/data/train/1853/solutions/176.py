class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        THRESHOLD_MAX = 10001
        dist = [[THRESHOLD_MAX for _ in range(n)] for _ in range(n)]

        for edge in edges:
            dist[edge[0]][edge[1]] = edge[2]
            dist[edge[1]][edge[0]] = edge[2]

        for i in range(n):
            dist[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i != j:
                        intermediate_dist = dist[i][k] + dist[k][j]
                        if intermediate_dist < dist[i][j]:
                            dist[i][j] = intermediate_dist

        min_threshold_cities = n
        curr = -1
        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    count += 1

            if count <= min_threshold_cities:
                min_threshold_cities = count
                curr = i
        return curr
