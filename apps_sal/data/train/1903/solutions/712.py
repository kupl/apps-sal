from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        G = defaultdict(dict)
        for i, (xi, yi) in enumerate(points):
            for j, (xj, yj) in enumerate(points[i + 1:], i + 1):
                d = abs(xi - xj) + abs(yi - yj)
                G[i][j] = G[j][i] = d
        seen, pq, ans = {0}, [], 0
        for nb, d in G[0].items():
            heappush(pq, (d, nb))
        while len(seen) < len(G):
            while pq:
                cost, next_node = heappop(pq)
                if next_node in seen:
                    continue
                seen.add(next_node)
                ans += cost
                for nb, d in G[next_node].items():
                    if nb in seen:
                        continue
                    heappush(pq, (d, nb))
        return ans
