import heapq
from collections import defaultdict
class Solution:
    def findTheCity(self, n: int, edges, distanceThreshold: int) -> int:
        matrix = [[float('inf')]*n for _ in range(n)]
        graph = defaultdict(list)
        for s, e, d in edges:
            matrix[s][e] = d
            matrix[e][s] = d
            graph[s].append(e)
            graph[e].append(s)
        # print(graph)
        # print(matrix)

        def dijkstra(source):
            dist = [float('inf')]*n
            dist[source] = 0
            pq = [(0, source)]
            heapq.heapify(pq)
            while pq:
                # print(pq)
                d, node = heapq.heappop(pq)
                if d > dist[node]:
                    continue
                for next_node in graph[node]:
                    tmp = d + matrix[node][next_node]
                    if tmp < dist[next_node]:
                        dist[next_node] = tmp
                        heapq.heappush(pq, (tmp, next_node))
            # print(source, dist)
            return sum(d <= distanceThreshold for d in dist) - 1

        res, counts = 0, n
        for i in range(n):
            tmp = dijkstra(i)
            # print(tmp, i)
            if tmp <= counts:
                counts = tmp
                res = i
        return res

