class Solution:

    def minCostConnectPoints(self, p: List[List[int]]) -> int:
        (edges, n, cnt, ans) = ([], len(p), 1, 0)

        def manhattan(x, y):
            return abs(p[x][0] - p[y][0]) + abs(p[x][1] - p[y][1])
        edges = [(manhattan(i, j), (i, j)) for i in range(n) for j in range(i + 1, n)]
        heapq.heapify(edges)

        def union(x, y):
            uf[find(x)] = find(y)

        def find(x):
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]
        uf = list(range(n))
        while cnt < n:
            (d, (u, v)) = heapq.heappop(edges)
            if find(u) != find(v):
                ans += d
                cnt += 1
                union(u, v)
        return ans
