class order(tuple):
    def __lt__(a, b):
        return a[0] < b[0]


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = {}
        edges, n, ans = [], len(points), 0
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))

        parent = [i for i in range(n)]
        rank = [0 for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            x, y = find(x), find(y)
            if rank[x] > rank[y]:
                parent[y] = x
            else:
                parent[x] = y

            if rank[x] == rank[y]:
                rank[x] += 1
            return
        edges = sorted(edges, key=order)
        for d, u, v in edges:
            x, y = find(u), find(v)
            if x != y:
                union(x, y)
                ans += d
        return ans
