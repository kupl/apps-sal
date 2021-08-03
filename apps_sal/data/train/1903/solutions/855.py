class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Tried brute force, failed on ensuring connectivity
        # Tried all pairs shortest path, not applicable
        # Remembered MSTs and Kruskal's, implemented here after competition
        def l1(p1, p2):
            xi, yi = p1
            xj, yj = p2
            return abs(xi - xj) + abs(yi - yj)

        inf = float('inf')
        LV = len(points)
        E = [(u, v, l1(points[u], points[v]))
             for u in range(LV) for v in range(LV) if u != v]
        E = sorted(E, key=lambda x: x[2])
        parent = [0] * LV

        def make_set(v):
            parent[v] = v

        def find_set(v):
            if v == parent[v]:
                return v
            parent[v] = find_set(parent[v])
            return parent[v]

        def union_sets(a, b):
            a = find_set(a)
            b = find_set(b)
            if a != b:
                parent[b] = a

        for v in range(LV):
            make_set(v)

        cost = 0
        for (u, v, d) in E:
            if (a := find_set(u)) != (b := find_set(v)):
                cost += d
                union_sets(a, b)

        return cost
