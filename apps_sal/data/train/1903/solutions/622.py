class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        cost = []
        for i in range(n):
            for j in range(i + 1, n):
                if i != j:
                    (x1, y1) = points[i]
                    (x2, y2) = points[j]
                    cost.append([abs(x1 - x2) + abs(y1 - y2), i, j])
        cost.sort()
        parent = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        def find(parent, i):
            if parent[i] == i:
                return i
            return find(parent, parent[i])

        def union(parent, rank, x, y):
            xroot = find(parent, x)
            yroot = find(parent, y)
            if rank[xroot] < rank[yroot]:
                parent[xroot] = yroot
            elif rank[xroot] > rank[yroot]:
                parent[yroot] = xroot
            else:
                parent[yroot] = xroot
                rank[xroot] += 1
        (i, e) = (0, 0)
        ans = 0
        while e < n - 1:
            (w, u, v) = cost[i]
            i += 1
            x = find(parent, u)
            y = find(parent, v)
            if x != y:
                e = e + 1
                ans += w
                union(parent, rank, x, y)
        return ans
