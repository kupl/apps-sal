class Solution:
    # copied from https://leetcode.com/problems/find-longest-awesome-substring/discuss/779893/C%2B%2BJavaPython3-with-picture-(similar-to-1371)
    def longestAwesome(self, s: str) -> int:
        mask, res = 0, 0
        dp = [-1] + [len(s)] * 1023
        for i in range(len(s)):
            mask ^= 1 << (ord(s[i]) - 48)
            for j in range(11):
                check_mask = 1023 & (mask ^ (1 << j))
                res = max(res, i - dp[check_mask])
            dp[mask] = min(dp[mask], i)
        return res
    
    def longestAwesome1(self, s: str) -> int:
        mask, res = 0, 0
        dp = [-1] + [len(s)] * 1023
        for i in range(len(s)):
            mask ^= 1 << (ord(s[i]) - 48)
            res = max(res, i - dp[mask])
            for j in range(10):
                res = max(res, i - dp[mask ^ (1 << j)])
            dp[mask] = min(dp[mask], i)
        return res
