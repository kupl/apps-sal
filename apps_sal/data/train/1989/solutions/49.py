class Solution:
    def longestAwesome(self, s: str) -> int:
        seen, prefix, ans = {0: -1}, 0, 0
        for i, char in enumerate(s):
            prefix ^= (1 << int(char))
            ans = max(ans, i - seen.get(prefix, float('inf')))
            for j in range(10):
                p = prefix ^ (1 << j)
                ans = max(ans, i - seen.get(p, float('inf')))
            if prefix not in seen:
                seen[prefix] = i
        return ans

