import sys


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = arr = [[10001 if i != j else 0 for i in range(n)] for j in range(n)]

        for source, target, weight in edges:
            dist[source][target] = weight
            dist[target][source] = weight

        for node in range(n):
            for source in range(n):
                for target in range(n):
                    new_dist = dist[source][node] + dist[node][target]
                    dist[source][target] = min(dist[source][target], new_dist)

        ncity = [n] * n
        for dindex, dlist in enumerate(dist):
            ncity[dindex] = [index for index, i in enumerate(dlist) if i <= distanceThreshold and i != 0]

        for source, cities in enumerate(ncity):
            for target in cities:
                if source not in ncity[target]:
                    ncity[target].append(source)

        min_count = 10001
        index = 0
        for cindex, city in enumerate(ncity):
            len_city = len(city)
            if len_city <= min_count:
                min_count = len_city
                index = cindex
        return index
