class Solution:

    def longestAwesome(self, s: str) -> int:
        d = {}
        d[0] = -1
        mask = 0
        ans = 0
        for (i, ch) in enumerate(s):
            mask ^= 1 << int(ch)
            if mask in d and (i - d[mask]) % 2 == 0:
                ans = max(ans, i - d[mask])
            for j in range(10):
                mask_edit = mask ^ 1 << j
                if mask_edit in d and (i - d[mask_edit]) % 2 == 1:
                    ans = max(ans, i - d[mask_edit])
            if mask not in d:
                d[mask] = i
        return ans
