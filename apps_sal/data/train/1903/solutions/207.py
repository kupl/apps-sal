class Solution:

    def minCostConnectPoints(self, p: List[List[int]]) -> int:
        (cur, N, ans) = (0, len(p), 0)
        dis = [float('inf')] * N
        seen = [False] * N
        for _ in range(N - 1):
            (x, y) = p[cur]
            seen[cur] = True
            for (j, (nx, ny)) in enumerate(p):
                if seen[j]:
                    continue
                dis[j] = min(dis[j], abs(nx - x) + abs(ny - y))
            (d, cur) = min(((w, k) for (k, w) in enumerate(dis)))
            dis[cur] = float('inf')
            ans += d
        return ans
