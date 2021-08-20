class Solution:

    def lastStoneWeightII(self, stones: List[int]) -> int:

        def dp(i, j):
            if i == N:
                return j
            if (i, j) in memo:
                return memo[i, j]
            memo[i, j] = min(dp(i + 1, abs(j + stones[i])), dp(i + 1, abs(j - stones[i])))
            return memo[i, j]
        memo = {}
        N = len(stones)
        return dp(0, 0)
