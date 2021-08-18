from heapq import *


class Solution:
    def minCostConnectPoints(self, points):
        N = len(points)
        parent = [i for i in range(N)]

        def find(v):
            while parent[v] != parent[parent[v]]:
                parent[v] = parent[parent[v]]
            return parent[v]

        def dist(p1, p2): return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        heap, total_cost = [], 0
        for u in range(N - 1):
            for v in range(u + 1, N):
                heappush(heap, [dist(points[u], points[v]), u, v])
        while heap:
            cost, u, v = heappop(heap)
            pu, pv = find(u), find(v)
            if pu != pv:
                parent[pu] = pv
                N -= 1
                total_cost += cost
                if N == 0:
                    break
        return total_cost


class Solution:
    def minCostConnectPoints(self, points):
        def dist(p1, p2): return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        N = len(points)
        points = sorted(points, key=lambda x: abs(x[0]) + abs(x[1]))
        parent = [i for i in range(N)]

        def find(v):
            while parent[v] != parent[parent[v]]:
                parent[v] = parent[parent[v]]
            return parent[v]
        heap = []
        for i in range(N - 1):
            for j in range(i + 1, N):
                heappush(heap, (dist(points[i], points[j]), i, j))
        res = 0
        while heap:
            d, u, v = heappop(heap)
            pu, pv = find(u), find(v)
            if pu != pv:
                parent[pu] = pv
                res += d
                N -= 1
                if N == 0:
                    break
        return res
