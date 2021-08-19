class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        parent = list(range(N))

        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            (x, y) = (find(u), find(v))
            if x != y:
                parent[y] = x
            return x != y
        edges = []
        for i in range(N):
            for j in range(i + 1, N):
                d = abs(points[i][0] - points[j][0])
                d += abs(points[i][1] - points[j][1])
                edges.append((d, i, j))
        total = 0
        for (cost, u, v) in sorted(edges):
            if union(u, v):
                total += cost
        return total
