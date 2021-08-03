class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0
        mx = -1
        inc = set()
        d = {}
        parent = []
        rank = []
        result = []
        i = 0
        e = 0
        nodes = {}
        idx = 0
        for i in range(n):
            nodes[idx] = (points[i][0], points[i][1])
            idx += 1
        graph = []
        for i in range(n):
            d[i] = []
            for j in range(n):
                if i == j:
                    continue
                graph.append([i, j, abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])])
        graph.sort(key=lambda x: x[2])

        def find(parent, i):
            if parent[i] == i:
                return i
            return find(parent, parent[i])

        def union(parent, rank, x, y):
            xroot = find(parent, x)
            yroot = find(parent, y)

            if rank[xroot] < rank[yroot]:
                parent[xroot] = yroot
            elif rank[yroot] < rank[xroot]:
                parent[yroot] = xroot
            else:
                parent[yroot] = xroot
                rank[xroot] += 1

        for node in range(n):
            parent.append(node)
            rank.append(0)
        i = 0
        ans = 0
        while e < n - 1:
            u, v, w = graph[i]
            i += 1
            x = find(parent, u)
            y = find(parent, v)
            if x != y:
                e = e + 1
                ans += w
                union(parent, rank, x, y)
        return ans
