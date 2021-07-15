class Solution:
  def stoneGameII(self, piles: List[int]) -> int:
    n = len(piles)
    dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    s = sum(piles)
    def helper(st, M):
      nonlocal n, piles, dp
      if st >= n:
        return 0
      if dp[M][st] != -1:
        return dp[M][st]
      cur = 0
      tmp = float('-inf')
      for x in range(1, 2*M+1):
        if st + x > n:
          continue
        
        tmp = max(tmp, sum(piles[st: st+x]) - helper(st+x, max(M, x)))
                  
      dp[M][st] = tmp 
      return tmp
    return int((helper(0,1) + s)/2)
      

