class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(a):
            if parents[a] != a:
                return find(parents[a])
            return a

        def union(a, b):
            xa = find(a)
            xb = find(b)
            if xa == xb:
                return
            if rank[xa] > rank[xb]:
                parents[xb] = xa

            elif rank[xa] < rank[xb]:
                parents[xa] = xb
            else:
                parents[xa] = xb
                rank[xb] += 1
        n = len(points)
        parents = [i for i in range(n)]
        rank = [i for i in range(n)]
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))
        edges.sort()

        res = 0

        for cost, u, v in edges:
            if find(u) != find(v):
                union(u, v)
                res += cost

        return res
