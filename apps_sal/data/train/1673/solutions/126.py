class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        dp = copy.deepcopy(arr)
        for i in range(1, len(dp)):
            r = heapq.nsmallest(2, dp[i - 1])
            for j in range(len(dp[0])):
                dp[i][j] += r[1] if dp[i - 1][j] == r[0] else r[0]
        return min(dp[-1])
