class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        cost = 0
        if n <= 1:
            return 0
        g = []
        for i in range(n):
            x1 = points[i][0]
            y1 = points[i][1]
            for j in range(i + 1, n):
                if j != i:
                    x2 = points[j][0]
                    y2 = points[j][1]
                    d = abs(x1 - x2) + abs(y1 - y2)
                    g.append([i, j, d])
        g.sort(key=lambda x: x[2])
        par = [-1] * n
        for (i, (u, v, c)) in enumerate(g):
            p1 = u
            while par[p1] > 0:
                p1 = par[p1]
            p2 = v
            while par[p2] > 0:
                p2 = par[p2]
            if p1 == p2:
                continue
            else:
                if abs(par[p1]) > abs(par[p2]):
                    par[p1] += par[p2]
                    if u != p1:
                        par[u] = p1
                    par[v] = p1
                    par[p2] = p1
                else:
                    par[p2] += par[p1]
                    if v != p2:
                        par[v] = p2
                    par[u] = p2
                    par[p1] = p2
                cost += c
        return cost
