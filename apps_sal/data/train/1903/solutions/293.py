class Solution:
    def minCostConnectPoints(self, points):
        distance = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        points.sort(key = lambda p: p[0] + p[1])
        total_cost = 0
        points = [[p, distance(p, points[0])] for p in points]
        while points:
            minIdx, mindist = None, float('inf')
            for i, (p1, dist) in enumerate(points):
                if dist < mindist:
                    minIdx, mindist = i, dist
            p1, cost = points.pop(minIdx)
            total_cost += cost
            for i, (p2, dist) in enumerate(points):
                points[i][1] = min(points[i][1], distance(p1, p2))
        return total_cost
    
from heapq import *
class Solution:
    def minCostConnectPoints(self, points):
        N = len(points)
        parent = [i for i in range(N)]
        def find(v):
            while parent[v] != parent[parent[v]]:
                parent[v] = parent[parent[v]]
            return parent[v]
        dist = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        connections = [[u, v, dist(points[u], points[v])] for u in range(N-1) for v in range(u+1, N)]
        connections.sort(key = lambda x:x[2])
        total_cost, remain = 0, N-1
        for u, v, cost in connections:
            pu, pv = find(u), find(v)
            if pu != pv:
                parent[pu] = pv
                total_cost += cost
                remain -= 1
                if remain == 0:
                    break
        return total_cost
