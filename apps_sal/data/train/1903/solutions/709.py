from collections import defaultdict
import heapq


class Solution:
    def minCostConnectPoints(self, points) -> int:
        edges = defaultdict(list)
        n = len(points)
        connected_pts = set([0])
        pending_edges = []
        for i in range(n):
            for j in range(i + 1, n):
                w = abs(points[j][1] - points[i][1]) + abs(points[j][0] - points[i][0])
                edges[i].append((w, j))
                edges[j].append((w, i))
        for e in edges[0]:
            heapq.heappush(pending_edges, (e[0], e[1]))

        res = 0
        while len(connected_pts) < n:
            found_edge = False
            while not found_edge:
                e = heapq.heappop(pending_edges)
                if e[1] in connected_pts:
                    continue
                found_edge = True
                connected_pts.add(e[1])
                res += e[0]
                for next_edge in edges[e[1]]:
                    if next_edge not in connected_pts:
                        heapq.heappush(pending_edges, (next_edge[0], next_edge[1]))
        return res
