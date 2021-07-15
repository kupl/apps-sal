class Solution:
  def countRoutes(self, x: List[int], start: int, finish: int, fuel: int) -> int:    
    @lru_cache(None)
    def dp(i, f): # ways to reach |finsh| from |i| with |f| fuel.
      if f < 0: return 0
      return (sum(dp(j, f - abs(x[i] - x[j])) 
                 for j in range(len(x)) if i != j) + (i == finish)) % (10**9 + 7)
    return dp(start, fuel)

