from heapq import heappush, heappop


class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        def dijkstra(graph, start, distance):
            reached = set()
            heap = [(0, start)]
            while heap:
                (w, node) = heappop(heap)
                if node in reached:
                    continue
                if w > distance:
                    continue
                if node != start:
                    reached.add(node)
                for (nex, nex_w) in graph[node]:
                    heappush(heap, (w + nex_w, nex))
            return reached
        graph = collections.defaultdict(set)
        for (x, y, w) in edges:
            graph[x].add((y, w))
            graph[y].add((x, w))
        min_len = n
        min_city = 0
        for i in range(n):
            reached = dijkstra(graph, i, distanceThreshold)
            if len(reached) <= min_len:
                min_len = len(reached)
                min_city = i
        return min_city
