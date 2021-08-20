class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        def union(x, y):
            id_x = find(x)
            id_y = find(y)
            if id_x == id_y:
                return 0
            if rank[id_x] == rank[id_y]:
                parent[id_y] = id_x
                rank[id_x] += 1
            elif rank[id_x] > rank[id_y]:
                parent[id_y] = id_x
            else:
                parent[id_x] = id_y
            return 1
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                edges.append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))
        edges = sorted(edges, key=lambda x: x[0])
        cost = 0
        for edge in edges:
            if union(edge[1], edge[2]):
                cost += edge[0]
        return cost
