class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = collections.defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = w
            graph[v][u] = w

        def dijstra(start, distanceThreshold):
            heap = [(0, start)]
            des = []
            while heap:
                w, u = heapq.heappop(heap)
                if u not in d:
                    d[u] = w
                    for v in graph[u]:
                        if graph[u][v] + d[u] <= distanceThreshold:
                            heapq.heappush(heap, (graph[u][v] + d[u], v))
                            if v not in des and v != start:
                                des.append(v)
            return len(des)

        res, count = 0, n
        for i in range(n):
            d = {}
            des = dijstra(i, distanceThreshold)
            if des <= count:
                res = max(res, i)
                count = des
        return res
