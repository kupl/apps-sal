import collections


class Solution:

    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        graph = collections.defaultdict(dict)
        for (i, j, w) in edges:
            graph[i][j] = graph[j][i] = w
        pq = [(0, 0)]
        used = {}
        dist = {0: 0}
        res = 0
        while pq:
            (d, v) = heapq.heappop(pq)
            if d > dist[v]:
                continue
            res += 1
            for (nei, weight) in list(graph[v].items()):
                use_wei = min(weight, M - d)
                used[v, nei] = use_wei
                d_min = d + weight + 1
                if d_min < dist.get(nei, M + 1):
                    dist[nei] = d_min
                    heapq.heappush(pq, (d_min, nei))
        for (i, j, w) in edges:
            res += min(w, used.get((i, j), 0) + used.get((j, i), 0))
        return res
