class Solution:
    def minCostConnectPoints(self, p: List[List[int]]) -> int:
        n = len(p)

        def find(x):
            if dp[x] != x:
                dp[x] = find(dp[x])
            return dp[x]

        def uni(x, y):
            x, y = find(x), find(y)
            if x != y:
                dp[x] = find(y)
                return False
            else:
                return True

        dp = list(range(n))

        pool = sorted((abs(p[i][0] - p[j][0]) + abs(p[i][1] - p[j][1]), i, j) for i in range(n) for j in range(i + 1, n))

        res = 0

        for dis, u, v in pool:
            if not uni(u, v):
                res += dis
        return res
