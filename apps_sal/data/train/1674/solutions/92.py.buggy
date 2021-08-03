\"\"\"
dp[i][j] = the max score one can get with [i:] piles and M = j.
dp[i][j] = max(sum[i:x] for x in range(1, min(2*M, n) - dp[i+x][max(M, x)])
dp[i][n] = sum(piles[i:])
\"\"\"
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suf_sum = [0 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            suf_sum[i] = suf_sum[i+1] + piles[i]
            
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][n] = suf_sum[i]
        
        for i in range(n, -1, -1):
            for j in range(n, 0, -1):
                for x in range(1, min(2*j, n - i) + 1):
                    dp[i][j] = max(dp[i][j], suf_sum[i] - dp[i+x][max(j, x)])
        return dp[0][1]
