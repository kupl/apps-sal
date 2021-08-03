class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((d, i, j))
        edges.sort()
        parent = {i: i for i in range(len(points))}

        def find(x):
            if not parent[x] == x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            par_x = find(x)
            par_y = find(y)
            if not par_x == par_y:
                parent[par_x] = parent[par_y]
                return True
            return False
        res = 0
        for d, u, v in edges:
            if union(u, v):
                res += d
        return res
