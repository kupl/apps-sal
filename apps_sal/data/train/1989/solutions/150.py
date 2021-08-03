class Solution:
    def longestAwesome(self, s: str) -> int:
        if s == s[::-1]:
            return len(s)
        pattern, re = 0, 0
        exit = {pattern: -1}

        for idx, val in enumerate(s):
            pattern ^= 1 << int(val)

            for k in range(10):
                new_pattern = pattern ^ (1 << k)

                re = max(re, idx - exit.get(new_pattern, idx))
            re = max(re, idx - exit.get(pattern, idx))
            exit.setdefault(pattern, idx)
        return re
