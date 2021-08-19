class Solution:

    def kruskal(self, n, edges):

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            (px, py) = (find(x), find(y))
            if px == py:
                return (False, False)
            parent[px] = py
            rank[py] += rank[px]
            return (True, True) if rank[py] == n else (True, False)
        mst_cost = 0
        parent = list(range(n))
        rank = [0] * n
        for (f, t, w) in edges:
            (isUnion, isEnd) = union(f, t)
            if isUnion:
                mst_cost += w
            if isEnd:
                break
        return mst_cost

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def manhattan(xx, yy):
            return abs(xx[0] - yy[0]) + abs(xx[1] - yy[1])
        if (n := len(points)) == 1:
            return 0
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                (x, y) = (points[i], points[j])
                edges.append([i, j, manhattan(x, y)])
        edges.sort(key=lambda x: x[2])
        return self.kruskal(n, edges)
