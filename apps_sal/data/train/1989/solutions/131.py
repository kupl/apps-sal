class Solution:

    def longestAwesome(self, s: str) -> int:
        (mask, res) = (0, 0)
        dp = [-1] + [len(s)] * 1023
        for i in range(len(s)):
            mask ^= 1 << ord(s[i]) - ord('0')
            res = max(res, i - dp[mask])
            for j in range(10):
                check_mask = 1023 & (mask ^ 1 << j)
                res = max(res, i - dp[check_mask])
            dp[mask] = min(dp[mask], i)
        return res
