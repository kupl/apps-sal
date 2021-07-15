from functools import lru_cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # dp[i,m] = max stones the current player can take from piles[i:] with M = m
        # which means 1 <= x <= 2M
        # use backwards prefix sum A[i] = totel stones of piles[i:]
        # means how many more the current player can take for max
        # the other player stones dp[i+x, max(m,x)]
        # the current player stone = A[i] - dp[i+x, max(m,x)]
        
        N = len(piles)
        for i in range(N-2, -1, -1):
          piles[i] += piles[i+1]
        
        @lru_cache(None)
        def dp(i, m):
          if i + 2*m >= N:
            return piles[i] # take as many as possible
          min_left = float('inf')
          for x in range(1, 2*m+1):
            min_left = min(min_left, dp(i+x, max(m, x)))
          return piles[i] - min_left
        
        return dp(0,1)
