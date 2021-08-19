class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        next_city = [[None] * n for _ in range(n)]
        for edge in edges:
            dist[edge[0]][edge[1]] = edge[2]
            dist[edge[1]][edge[0]] = edge[2]
            next_city[edge[0]][edge[1]] = edge[1]
        for city in range(n):
            dist[city][city] = 0
            next_city[city][city] = city
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        next_city[i][j] = next_city[i][k]
        city_sum_under_thresh = [0] * n
        for i in range(n):
            city_sum_under_thresh[i] += len([distance for (index, distance) in enumerate(dist[i]) if distance <= distanceThreshold if index != i])
        return min([(index, count) for (index, count) in enumerate(city_sum_under_thresh)], key=lambda x: (x[1], -x[0]))[0]
