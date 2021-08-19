class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        (n, ans, curr) = (len(points), 0, 0)
        (costs, used) = ([math.inf] * n, set())
        for i in range(1, n):
            (x, y) = points[curr]
            used.add(curr)
            for j in range(n):
                if j in used:
                    continue
                (u, v) = points[j]
                costs[j] = min(costs[j], abs(u - x) + abs(v - y))
            (cost, curr) = min(((x, i) for (i, x) in enumerate(costs)))
            ans += cost
            costs[curr] = math.inf
        return ans
