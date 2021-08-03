class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(parent, i):
            if parent[i] == i:
                return i
            return find(parent, parent[i])

        def apply_union(parent, rank, x, y):
            xroot = find(parent, x)
            yroot = find(parent, y)
            if rank[xroot] < rank[yroot]:
                parent[xroot] = yroot
            elif rank[xroot] > rank[yroot]:
                parent[yroot] = xroot
            else:
                parent[yroot] = xroot
                rank[xroot] += 1

        ans = 0
        V = len(points)
        graph = []
        for i in range(V):
            for j in range(i):
                v = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph.append([i, j, v])

        i, e = 0, 0
        graph = sorted(graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(V):
            parent.append(node)
            rank.append(0)
        while e < V - 1:
            u, v, w = graph[i]
            i = i + 1
            x = find(parent, u)
            y = find(parent, v)
            if x != y:
                e = e + 1
                ans += w
                apply_union(parent, rank, x, y)
        return ans
