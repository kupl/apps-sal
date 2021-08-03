from queue import PriorityQueue
import math
from collections import defaultdict


class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        adj = defaultdict(list)  # list (adj_vertex, edge_weight)
        for x, y, n in edges:
            adj[x].append([y, n + 1])
            adj[y].append([x, n + 1])
        q = PriorityQueue()  # (dist, vertex)
        dist = [math.inf for _ in range(N)]
        dist[0] = 0
        q.put([0, 0])
        while not q.empty():
            d, x = q.get()
            for y, w in adj[x]:
                if d + w <= M and d + w < dist[y]:
                    dist[y] = d + w
                    q.put([dist[y], y])
        cnt = len([1 for d in dist if d < math.inf])
        for x, y, n in edges:
            c1 = M - dist[x] if dist[x] < math.inf else 0
            c2 = M - dist[y] if dist[y] < math.inf else 0
            cnt += min(n, c1 + c2)
        return cnt
