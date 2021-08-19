class Solution:

    def circularPermutation(self, n: int, start: int) -> List[int]:
        dp = [i ^ i >> 1 for i in range(1 << n)]
        idx = dp.index(start)
        return dp[idx:] + dp[:idx]
