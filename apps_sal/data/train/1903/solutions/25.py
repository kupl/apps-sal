class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, curr, ans = len(points), 0, 0  # curr is a random point as the base of the MST
        cost = [math.inf] * n  # the minimum cost to add point i to form the MST
        used = set()
        for i in range(n - 1):  # n - 1 is because we need n - 1 edges totally
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
