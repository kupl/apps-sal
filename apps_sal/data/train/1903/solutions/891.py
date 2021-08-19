class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        root = list(range(N))
        size = [1] * N
        res = 0

        def find(x):
            root[x] = find(root[x]) if root[x] != x else root[x]
            return root[x]

        def union(x, y):
            (x, y) = (find(x), find(y))
            if x == y:
                return False
            if size[x] < size[y]:
                (x, y) = (y, x)
            root[y] = x
            size[x] += size[y]
            return True
        edge_ls = []
        for (i, cur) in enumerate(points):
            for (j, nxt) in enumerate(points[i + 1:]):
                dist = abs(cur[0] - nxt[0]) + abs(cur[1] - nxt[1])
                edge_ls.append([dist, i, i + j + 1])
        edge_ls.sort()
        for (dist, u, v) in edge_ls:
            if find(u) != find(v):
                res += dist
                union(u, v)
        return res
