from typing import List
from heapq import heappop, heappush


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = [False] * len(points)
        cost = 0
        pq = [(0, 0)]
        def get_dist(i, j): return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        while pq:
            dist, node = heappop(pq)
            if visited[node]:
                continue
            else:
                visited[node] = True
            cost += dist
            for adj in range(len(points)):
                if not visited[adj]:
                    heappush(pq, (get_dist(node, adj), adj))
        return cost
