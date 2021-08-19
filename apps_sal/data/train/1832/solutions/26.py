from collections import defaultdict, deque
import heapq


class Solution:

    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        d = defaultdict(set)
        for edge in edges:
            d[edge[0]].add((edge[1], edge[2] + 1))
            d[edge[1]].add((edge[0], edge[2] + 1))
        q = [(0, 0)]
        visited = defaultdict(lambda: float('inf'))
        visited[0] = 0
        sd = defaultdict(int)
        while len(q) > 0:
            (m, cur) = heapq.heappop(q)
            for (adj, dis) in d[cur]:
                if visited[adj] > m + dis and m + dis <= M:
                    heapq.heappush(q, (m + dis, adj))
                    visited[adj] = m + dis
                sd[cur, adj] = max(sd[cur, adj], min(dis - 1, M - m))
        ans = len([x for x in list(visited.values()) if x != float('inf')])
        for (a, b, c) in edges:
            ans += min(sd[a, b] + sd[b, a], c)
        return ans
