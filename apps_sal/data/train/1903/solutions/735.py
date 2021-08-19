class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((d, i, j))
        edges.sort()
        root = [i for i in range(n)]

        def find(v):
            if root[v] != v:
                root[v] = find(root[v])
            return root[v]

        def union(u, v):
            p1 = find(u)
            p2 = find(v)
            if p1 != p2:
                root[p2] = root[p1]
                return True
            return False
        res = 0
        for (d, u, v) in edges:
            if union(u, v):
                res += d
        return res
