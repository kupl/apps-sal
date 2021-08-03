class Solution:
    def minCostConnectPoints(self, p: List[List[int]]) -> int:

        def manhattan(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])

        cur, N, ans = 0, len(p), 0
        dis = [float('inf')] * N
        seen = set()

        for _ in range(N - 1):
            seen.add(cur)
            for j in range(N):
                if j in seen:
                    continue
                dis[j] = min(dis[j], manhattan(p[cur], p[j]))

            d, cur = min((w, k) for k, w in enumerate(dis))
            dis[cur] = float('inf')
            ans += d

        return ans
