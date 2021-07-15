class Solution:
    def longestAwesome(self, s: str) -> int:
        ans = 1
        mask = 0
        memo = { 0:-1 }
        for idx, ch in enumerate(s):
            mask = mask ^ (1 << int(ch))
            if mask in memo:
                ans = max(ans, idx - memo[mask])
            for i in range(10):
                check = mask ^ (1 << i)
                if check in memo:
                    ans = max(ans, idx - memo[check])
            if not mask in memo:
                memo[mask] = idx
        return ans
