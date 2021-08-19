class Solution:

    def longestAwesome(self, s: str) -> int:
        dp = {}
        dp[0] = -1
        (state, ans) = (0, 0)
        for (i, c) in enumerate(s):
            state ^= 1 << int(c)
            if state not in dp:
                dp[state] = i
            else:
                ans = max(ans, i - dp[state])
            for num in range(10):
                if state ^ 1 << num in dp:
                    ans = max(ans, i - dp[state ^ 1 << num])
        return ans
