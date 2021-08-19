import heapq


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        def find(i):
            if parent[i] < 0:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        res = 0
        n = len(points)
        parent = [-1] * n
        rank = [0] * n
        h = []
        for u in range(n):
            for v in range(u + 1, n):
                h.append((dist(points[u], points[v]), u, v))
        heapq.heapify(h)
        while h:
            (d, u, v) = heapq.heappop(h)
            (u, v) = (find(u), find(v))
            if u != v:
                res += d
                if rank[u] > rank[v]:
                    parent[u] += parent[v]
                    parent[v] = u
                else:
                    parent[v] += parent[u]
                    parent[u] = v
                    if rank[u] == rank[v]:
                        rank[v] += 1
                if parent[u] == -n:
                    break
        return res
