class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        a = points
        n = len(a)

        def d(i, j):
            return abs(a[i][0] - a[j][0]) + abs(a[i][1] - a[j][1])
        q = []
        dst = [float('inf')] * n
        vis = [False] * n

        def consider(du, u):
            if vis[u] or du >= dst[u]:
                return
            dst[u] = du
            heappush(q, (du, u))
        consider(0, 0)
        while q:
            (du, u) = heappop(q)
            if vis[u]:
                continue
            vis[u] = True
            for v in range(n):
                consider(d(u, v), v)
        return sum(dst)
