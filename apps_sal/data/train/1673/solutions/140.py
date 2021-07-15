class Solution:
    def minFallingPathSum(self, dp: List[List[int]]) -> int:
        for i in range(1, len(dp)):
            best2 = sorted(list(enumerate(dp[i-1])), key=lambda x: x[1])[:2]
            for j in range(len(dp[i])):
                dp[i][j] = [x for x in best2 if x[0] != j][0][1] + dp[i][j]

        return min(dp[-1])
