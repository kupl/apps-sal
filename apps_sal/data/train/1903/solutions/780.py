class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        edges = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                u, v = points[i]
                p, q = points[j]
                w = abs(p - u) + abs(q - v)
                edges.append((w, i, j))

        path = {u: u for u in range(n)}
        rank = {u: 0 for u in range(n)}

        def find(u: int) -> int:
            if u != path[u]:
                path[u] = find(path[u])
            return path[u]

        def union(u: int, v: int) -> None:
            i, j = find(u), find(v)
            if rank[i] > rank[j]:
                path[j] = i
            else:
                path[i] = j
                if rank[i] == rank[j]:
                    rank[i] += 1

        costs = 0
        edges.sort()
        for w, u, v in edges:
            if find(u) != find(v):
                costs += w
                union(u, v)
        return costs
