class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def find(x):
            if x == parent[x]:
                return x
            return find(parent[x])

        def union(p, q):
            x = find(p)
            y = find(q)
            if rank[x] < rank[y]:
                parent[x] = y
            elif rank[y] < rank[x]:
                parent[y] = x
            else:
                parent[y] = x
                rank[x] += 1
        n = len(points)
        graph = []
        parent = {}
        rank = {}
        for i in range(n):
            for j in range(i + 1, n):
                w = abs(points[j][1] - points[i][1]) + abs(points[j][0] - points[i][0])
                graph.append([i, j, w])
        edges = sorted(graph, key=lambda k: k[2])
        for i in range(n):
            parent[i] = i
            rank[i] = 0
        ans = 0
        for (x, y, w) in edges:
            if find(x) != find(y):
                ans += w
                union(x, y)
        return ans
