class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        l = len(points)
        h = []
        for i in range(l):
            for j in range(i):
                (x1, y1), (x2, y2) = points[i], points[j]
                dis = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(h, [dis, i, j])
        dp = [i for i in range(l)]

        def find(x):
            if dp[x] != x:
                dp[x] = find(dp[x])
            return dp[x]

        ans = 0
        while h:
            dis, x, y = heapq.heappop(h)
            if find(x) != find(y):
                ans += dis
            dp[find(x)] = find(y)

        return ans
