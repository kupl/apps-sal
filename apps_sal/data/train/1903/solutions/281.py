class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        if len(points) <= 1:
            return 0
        N = len(points)
        distances = [float('inf')] * N
        seen = set()
        ans = 0
        curr = 0
        for i in range(N - 1):
            x1, y1 = points[curr]
            seen.add(curr)
            for j in range(N):
                x2, y2 = points[j]
                if j in seen:
                    continue
                distances[j] = min(abs(x1 - x2) + abs(y1 - y2), distances[j])
            delta, curr = min((d, j) for j, d in enumerate(distances))
            distances[curr] = float('inf')
            ans += delta
        return ans
