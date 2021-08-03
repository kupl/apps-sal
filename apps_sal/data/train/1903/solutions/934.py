class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        edges = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                u, v = points[i]
                p, q = points[j]
                w = abs(u - p) + abs(v - q)
                edges.append([w, i, j])

        path = [u for u in range(n)]

        def find(u: int) -> int:
            if path[u] != u:
                path[u] = find(path[u])
            return path[u]

        def union(u: int, v: int) -> None:
            i, j = find(u), find(v)
            if i != j:
                if j > i:
                    i, j = j, i
                path[j] = i

        costs = 0
        edges.sort()
        for w, u, v in edges:
            if find(u) != find(v):
                costs += w
                union(u, v)
        return costs
