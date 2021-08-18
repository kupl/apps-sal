from collections import defaultdict


class Solution:
    def longestAwesome(self, s: str) -> int:
        n = len(s)
        dp = [n for i in range(1024)]
        dp[0] = -1
        mask, ret = 0, 0

        for i, c in enumerate(s):
            mask ^= (1 << int(c))
            for num in range(10):
                ret = max(ret, i - dp[mask ^ (1 << num)])
            ret = max(ret, i - dp[mask])
            dp[mask] = min(dp[mask], i)
        return ret
