import gc
from collections import defaultdict
gc.disable()


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[math.inf for _ in range(n)] for _ in range(n)]
        for source, sink, cost in edges:
            graph[source][sink] = cost
            graph[sink][source] = cost
        for k in range(n):
            for i in range(n):
                if i == k:
                    continue
                for j in range(n):
                    if i == j or j == k:
                        continue
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        counts_map = defaultdict(lambda: -1)
        for i in range(n):
            count = 0
            for x in graph[i]:
                if x <= distanceThreshold:
                    count += 1
            counts_map[count] = max(counts_map[count], i)
        return counts_map[min(counts_map.keys())]
