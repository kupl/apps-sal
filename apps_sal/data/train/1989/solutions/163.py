class Solution:

    def longestAwesome(self, s: str) -> int:
        dp = [-2] * 1024
        run = 0
        ans = 0
        dp[0] = -1
        for (j, i) in enumerate(s):
            k = int(i)
            run ^= 1 << k
            if dp[run] == -2:
                dp[run] = j
            else:
                ans = max(ans, j - dp[run])
            for k in range(10):
                if dp[run ^ 1 << k] != -2:
                    ans = max(ans, j - dp[run ^ 1 << k])
        return ans
