class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        (n, res) = (len(points), 0)
        if n <= 1:
            return res
        dists = [(abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j) for i in range(n - 1) for j in range(i + 1, n)]
        dists.sort()
        parents = list(range(n))

        def find(c):
            prec = c
            while parents[c] != c:
                c = parents[c]
            union(prec, c)
            return c

        def union(src, dst):
            if src != dst:
                parents[src] = dst
        for (d, src, dst) in dists:
            (ps, pd) = (find(src), find(dst))
            if ps != pd:
                res += d
                union(ps, pd)
        return res
