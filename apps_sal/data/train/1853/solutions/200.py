import sys
from heapq import heappush, heappop


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        def shortestPath(adj, V, src, k):
            heap = []
            dist = [sys.maxsize] * V
            dist[src] = 0

            heappush(heap, (0, src))

            while heap:
                u = heappop(heap)[1]

                for node in adj[u]:
                    v = node[0]
                    weight = node[1]

                    if dist[v] > dist[u] + weight:
                        dist[v] = dist[u] + weight
                        heappush(heap, (dist[v], v))

            count = 0
            for d in dist:
                if d <= k:
                    count += 1

            return count

        adj = collections.defaultdict(list)

        for val in edges:
            adj[val[0]].append((val[1], val[2]))
            adj[val[1]].append((val[0], val[2]))

        cities = [0] * n

        for i in range(n):
            cities[i] = shortestPath(adj, n, i, distanceThreshold)

        minVal = cities[0]
        minIndex = 0

        for i in range(1, n):
            if cities[i] <= minVal:
                minVal = cities[i]
                minIndex = i

        return minIndex
