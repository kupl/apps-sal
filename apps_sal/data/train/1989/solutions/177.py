class Solution:
    def longestAwesome(self, s: str) -> int:
        memo = {0: -1}
        max_len = 0
        mask = 0
        for i in range(len(s)):
            num = int(s[i])
            mask ^= (1 << num)
            if mask in memo:
                max_len = max(max_len, i - memo[mask])
            for j in range(10):
                if mask ^ (1 << j) in memo:
                    max_len = max(max_len, i - memo[mask ^ (1 << j)])
            if mask not in memo:
                memo[mask] = i
        return max_len
