from heapq import *
class Solution:
    def minCostConnectPoints(self, points):
        N = len(points)
        parent = [i for i in range(N)]
        def find(v):
            while parent[v] != parent[parent[v]]:
                parent[v] = parent[parent[v]]
            return parent[v]
        #dist = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        heap, total_cost = [], 0
        for i1, p1 in enumerate(points):
            for i2, p2 in enumerate(points[i1+1:], start = i1+1):
                #heappush(heap, (dist(p1, p2), i1, i2))
                heappush(heap, (abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]), i1, i2))
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

