class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        dp = arr[0][:]

        for i, costs in enumerate(arr[1:], 1):
            prev = dp[:]

            for j, cost in enumerate(costs):
                dp[j] = cost + min(prev[:j] + prev[j + 1:])

        return min(dp)
