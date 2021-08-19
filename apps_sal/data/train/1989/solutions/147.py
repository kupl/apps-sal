class Solution:

    def longestAwesome(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        dp = [-1] + [n] * 1023
        (mask, res) = (0, 0)
        for i in range(n):
            mask = mask ^ 1 << int(s[i])
            for j in range(11):
                ch_mask = 1023 & (mask ^ 1 << j)
                res = max(res, i - dp[ch_mask])
            dp[mask] = min(i, dp[mask])
        return res
