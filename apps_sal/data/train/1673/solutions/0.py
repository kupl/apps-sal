class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        dp = [0] * len(arr[0])
        for (r, row) in enumerate(arr):
            minNb = min(dp)
            min1 = dp.index(minNb)
            dp[min1] = float('inf')
            min2 = dp.index(min(dp))
            dp[min1] = minNb
            for c in range(len(row)):
                if c != min1:
                    row[c] += dp[min1]
                else:
                    row[c] += dp[min2]
            dp = row[:]
        return min(dp)
