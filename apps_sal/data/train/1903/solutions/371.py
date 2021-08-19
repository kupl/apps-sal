from collections import defaultdict


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        total_points = len(points)
        parent = list(range(total_points))
        weight_matrix = []

        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        for i in range(total_points):
            for j in range(i + 1, total_points):
                dist = manhattan(points[i], points[j])
                weight_matrix.append((i, j, dist))
        cost = 0
        for (u, v, w) in sorted(weight_matrix, key=lambda x: x[2]):
            (ru, rv) = (find(u), find(v))
            if ru == rv:
                continue
            cost += w
            parent[ru] = rv
        return cost
