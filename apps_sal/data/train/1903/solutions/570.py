class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        (N, g) = (len(points), [])
        res = 0
        for i in range(N - 1):
            (x0, y0) = points[i]
            for j in range(i + 1, N):
                (x1, y1) = points[j]
                dist = abs(x0 - x1) + abs(y0 - y1)
                g.append((dist, (i, j)))
        g.sort()
        parents = [None] * N
        for i in range(N):
            parents[i] = i

        def findParent(x):
            if parents[x] != x:
                parents[x] = findParent(parents[x])
            return parents[x]
        used_edges = 0
        for (w, (a, b)) in g:
            pa = findParent(a)
            pb = findParent(b)
            if pa != pb:
                res += w
                parents[pa] = pb
                used_edges += 1
                if used_edges == N - 1:
                    break
        return res
