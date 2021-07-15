class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        post = [0] * (n+1)
        for i in range(n-1, -1, -1):
            post[i] = post[i+1] + piles[i]
        
        dp = [[-1]*200 for _ in range(101)]
        
        def solve(i, m):
            if i >= len(piles):
                return 0
            if dp[i][m] > 0:
                return dp[i][m]
            s = ans = 0
            for di in range(1, 2*m+1):
                ii = i + di - 1
                if ii >= len(piles):
                    break
                s += piles[ii]
                other = solve(ii+1, max(m, di))
                ans = max(ans, s + post[ii+1] - other)
            dp[i][m] = ans
            return ans
        return solve(0, 1)

