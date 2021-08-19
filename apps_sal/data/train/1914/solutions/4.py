class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        dp = [0] + [float('inf')] * (N // 2)

        for i in range(1, N + 1):

            for j in range(N // 2, 0, -1):
                dp[j] = min(dp[j] + costs[i - 1][1], dp[j - 1] + costs[i - 1][0])
            dp[0] += costs[i - 1][1]
        # print(dp)
        return dp[-1]
