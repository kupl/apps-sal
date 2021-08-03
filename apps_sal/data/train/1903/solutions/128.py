class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        uf = {}

        def find(x):
            uf.setdefault(x, x)
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                uf[px] = py

        @lru_cache(None)
        def dist(i, j):
            x1, y1 = points[i]
            x2, y2 = points[j]
            return abs(x1 - x2) + abs(y1 - y2)

        n = len(points)
        hp = [(dist(i, j), i, j) for i in range(n) for j in range(i + 1, n)]
        heapq.heapify(hp)
        ans = 0

        while hp:
            d, i, j = heapq.heappop(hp)
            if find(i) != find(j):
                ans += d
                union(i, j)

        return ans


#         n = len(points)
#         U = {0}
#         V = set(range(n)) - U
#         ans = 0
#         while V:
#             cand = set()
#             mind = float(\"inf\")
#             for u in U:
#                 for v in V:
#                     if dist(u, v) < mind:
#                         mind = dist(u, v)
#                         tmp = v
#             ans += mind
#             U |= {tmp}
#             V -= {tmp}
#         return ans
