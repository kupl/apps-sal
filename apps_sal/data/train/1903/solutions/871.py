from heapq import *
from collections import defaultdict


class Solution:

    def minCostConnectPoints(self, points):

        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        points.sort(key=lambda p: p[0] + p[1])
        total_cost = 0
        points = [[p, distance(p, points[0])] for p in points]
        while points:
            (minIdx, mindist) = (None, float('inf'))
            for (i, (p1, dist)) in enumerate(points):
                if dist < mindist:
                    (minIdx, mindist) = (i, dist)
            (p1, cost) = points.pop(minIdx)
            total_cost += cost
            for (i, (p2, dist)) in enumerate(points):
                points[i][1] = min(points[i][1], distance(p1, p2))
        return total_cost


class Solution:

    def minCostConnectPoints(self, points):
        N = len(points)

        def dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        edges = defaultdict(list)
        for (i1, p1) in enumerate(points):
            for (i2, p2) in enumerate(points[i1 + 1:], start=i1 + 1):
                distance = dist(p1, p2)
                edges[i1].append([distance, i2])
                edges[i2].append([distance, i1])
        heap = edges[0]
        heapify(heap)
        (total_cost, seen) = (0, {0})
        while len(seen) < N:
            (cost, node) = heappop(heap)
            if node in seen:
                continue
            seen.add(node)
            total_cost += cost
            for (dist, next_) in edges[node]:
                if next_ not in seen:
                    heappush(heap, [dist, next_])
        return total_cost
