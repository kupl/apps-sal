import heapq
import pprint
from collections import defaultdict, deque


class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        adj_list = defaultdict(list)
        for x, y, n in edges:
            adj_list[x].append((y, n))
            adj_list[y].append((x, n))

        pq = [(0, 0)]
        visited_node = set()
        visited_edge = defaultdict(int)
        while pq:
            d, cur = heapq.heappop(pq)
            if d > M:
                break
            if cur in visited_node:
                continue

            visited_node.add(cur)
            for nxt, n in adj_list[cur]:
                visited_edge[(cur, nxt)] = max(
                    visited_edge[(cur, nxt)],
                    min(M - d, n + 1),
                )
                heapq.heappush(pq, (d + n + 1, nxt))

        count_visited_edge = sum(
            min(visited_edge[(x, y)] + visited_edge[(y, x)], n)
            for x, y, n in edges
        )
        return len(visited_node) + count_visited_edge

