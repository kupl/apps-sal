class Solution:
    def longestAwesome(self, s: str) -> int:
        idx = [-1] + [len(s)] * 1023
        ans, mask = 0, 0
        for i, c in enumerate(s):
            mask ^= 1 << (ord(c) - ord('0'))
            ans = max(ans, i - idx[mask])
            for j in range(10):
                ans = max(ans, i - idx[mask ^ (1 << j)])
            idx[mask] = min(i, idx[mask])
        return ans
