class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edge_costs = []
        for i in range(n):
            for j in range(i + 1, n):
                p1, p2 = points[i], points[j]
                cost = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                edge_costs.append((cost, (i, j)))

        edge_costs.sort()

        total = 0
        parent = list(range(n))

        def find_parent(v):
            if parent[v] == v:
                return v
            else:
                parent[v] = find_parent(parent[v])
                return parent[v]

        for cost, edge in edge_costs:
            v1, v2 = edge
            v1_parent = find_parent(v1)
            v2_parent = find_parent(v2)
            if v1_parent != v2_parent:
                total += cost
                parent[v2_parent] = v1_parent

        return total
