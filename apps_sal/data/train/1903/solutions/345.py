class Solution:

    def minCostConnectPoints(self, points):
        N = len(points)

        def dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        connections = [[u, v, dist(points[u], points[v])] for u in range(N - 1) for v in range(u + 1, N)]
        connections.sort(key=lambda x: x[2])
        (parent, cnt, res) = ([i for i in range(N + 1)], N - 1, 0)

        def find(v):
            while parent[v] != parent[parent[v]]:
                parent[v] = parent[parent[v]]
            return parent[v]
        for (u, v, cost) in connections:
            (pu, pv) = (find(u), find(v))
            if pu != pv:
                parent[pu] = pv
                cnt -= 1
                res += cost
                if cnt == 0:
                    break
        return res
