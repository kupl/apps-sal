class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = collections.defaultdict(dict)
        for (i, j, d) in edges:
            graph[i][j] = graph[j][i] = d

        def dikstra(node, distanceThreshold):
            visited = [False] * n
            dist = [float('inf')] * n
            heap = [(0, node)]
            while not all(visited) and heap:
                (distance, node) = heapq.heappop(heap)
                if distance > distanceThreshold:
                    break
                dist[node] = distance
                visited[node] = True
                for d in graph[node]:
                    if not visited[d]:
                        heapq.heappush(heap, (distance + graph[node][d], d))
            return len([i for i in dist if i <= distanceThreshold])
        res = 0
        count = n
        for i in range(n):
            c = dikstra(i, distanceThreshold)
            if c <= count:
                res = max(res, i)
                count = c
        return res
