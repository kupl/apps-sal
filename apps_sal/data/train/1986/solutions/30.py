class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        # dp = [0, 1]
        # for i in range(1, n):
        #     dp2 = dp + [d | 1 << i for d in dp[::-1]]
        #     dp = dp2
        # idx = dp.index(start)
        # return dp[idx:] + dp[: idx]
        
        # Alternatively, using Gray Code
        return [start ^ i ^ i >> 1 for i in range(1 << n)]
        

