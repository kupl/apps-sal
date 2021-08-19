class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[math.inf] * n for i in range(n)]
        for e in edges:
            dist[e[0]][e[1]] = e[2]
            dist[e[1]][e[0]] = e[2]
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        print(dist)
        max_city_numbers = n + 1
        selected_city = n
        for i in range(n - 1, -1, -1):
            city_numbers = 0
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    city_numbers += 1
            print(city_numbers)
            if city_numbers < max_city_numbers:
                max_city_numbers = city_numbers
                selected_city = i
        return selected_city
