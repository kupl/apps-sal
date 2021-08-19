import math
from collections import defaultdict
from queue import PriorityQueue


class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        adj = defaultdict(list)
        for x, y, w in edges:
            adj[x].append([y, w + 1])
            adj[y].append([x, w + 1])
        dist = [math.inf for _ in range(N)]
        q = PriorityQueue()  # queue of [dist, vertex_id]
        q.put([0, 0])
        dist[0] = 0
        while not q.empty():
            d, x = q.get()
            for y, w in adj[x]:
                if d + w <= M and dist[y] > d + w:
                    dist[y] = d + w
                    q.put([dist[y], y])
        cnt = len([1 for d in dist if d < math.inf])
        for x, y, w in edges:
            covered = 0
            if dist[x] < math.inf:
                covered += M - dist[x]
            if dist[y] < math.inf:
                covered += M - dist[y]
            cnt += min(w, covered)
        return cnt
