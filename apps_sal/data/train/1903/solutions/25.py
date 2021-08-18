class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, curr, ans = len(points), 0, 0
        cost = [math.inf] * n
        used = set()
        for i in range(n - 1):
            x, y = points[curr]
            used.add(curr)
            for j, (u, v) in enumerate(points):
                if j in used:
                    continue
                cost[j] = min(cost[j], abs(u - x) + abs(v - y))
            delta, curr = min((d, j) for j, d in enumerate(cost))
            cost[curr] = math.inf
            ans += delta
        return ans
