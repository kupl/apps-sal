class Solution:

    def lastStoneWeightII(self, arr: List[int]) -> int:
        upperBound = sum(arr) // 2
        dp = [[0 for i in range(upperBound + 1)] for j in range(len(arr))]
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if arr[i] <= j:
                    dp[i][j] = max(dp[i - 1][j - arr[i]] + arr[i], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]
        return sum(arr) - 2 * dp[-1][-1]
