class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # compute cost:
        n = len(points)
        g = []
        for i in range(n):
            for j in range(i + 1, n):
                w = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                g.append([i, j, w])
        g = sorted(g, key=lambda x: x[2])
        par = list(range(n))
        # print(par)
        # print(g)

        def root(i):
            while par[i] != i:
                par[i] = par[par[i]]
                i = par[i]
            return i

        def union(i, j):
            pi, pj = root(i), root(j)
            par[pi] = par[pj]
        cost = 0
        for i, j, w in g:
            if root(i) != root(j):
                cost += w
                # union i and j:
                union(i, j)

        return cost
