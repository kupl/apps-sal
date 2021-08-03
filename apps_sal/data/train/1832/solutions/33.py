class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        graph = collections.defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w + 1

        heap = [(-M, 0)]
        d = {}

        while heap:
            moves, u = heapq.heappop(heap)
            if u not in d:
                d[u] = -moves
                for v in graph[u]:
                    temp = -moves - graph[u][v]
                    if v not in d and temp >= 0:
                        heapq.heappush(heap, (-temp, v))

        res = len(d)
        for u, v, w in edges:
            res += min(d.get(u, 0) + d.get(v, 0), w)

        return res
