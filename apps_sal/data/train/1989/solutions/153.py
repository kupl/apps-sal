class Solution:

    def longestAwesome(self, s: str) -> int:
        max_val = 0
        seen = {0: -1}
        cur = 0
        for (i, char) in enumerate(s):
            cur ^= 1 << int(char)
            seen.setdefault(cur, i)
            max_val = max(max_val, i - seen[cur])
            for a in range(10):
                max_val = max(max_val, i - seen.get(cur ^ 1 << a, i))
        return max_val
