class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        dp = arr[0]
        n = len(arr[0])
        for row in arr[1:]:
            newdp = row[:]
            for i in range(n):
                temp = dp[:i] + dp[i + 1:]
                newdp[i] += min(temp)
            dp = newdp
        return min(dp)
