class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parent = {}
        size = defaultdict(lambda: 1)

        def find(u):
            if u != parent.get(u, u):
                parent[u] = find(parent[u])
            return parent.get(u, u)

        def union(u, v):
            (u, v) = (find(u), find(v))
            if u != v:
                if size[u] < size[v]:
                    (u, v) = (v, u)
                parent[u] = v
                size[u] += size[v]
        total = 0
        edges = []
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    edges.append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))
        edges.sort()
        for (cost, u, v) in edges:
            if find(u) != find(v):
                total += cost
                union(u, v)
        return total
