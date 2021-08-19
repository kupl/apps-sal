class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        weight_graph = []
        res = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                weight_graph.append([i, j, abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])])
        weight_graph = sorted(weight_graph, key=lambda item: item[2])
        parent = [i for i in range(n)]
        rank = [0 for _ in range(n)]

        def find(i):
            if parent[i] == i:
                return i
            else:
                return find(parent[i])

        def union(x, y):
            if rank[x] < rank[y]:
                parent[x] = parent[y]
            elif rank[x] > rank[y]:
                parent[y] = parent[x]
            else:
                parent[x] = parent[y]
                rank[y] += 1
        for edge in weight_graph:
            if len(res) < len(points) - 1:
                (u, v, w) = edge
                x = find(u)
                y = find(v)
                if x != y:
                    union(x, y)
                    res.append(w)
        if not res:
            return 0
        return sum(res)
