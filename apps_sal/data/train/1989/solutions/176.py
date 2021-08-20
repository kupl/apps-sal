class Solution:

    def longestAwesome(self, s: str) -> int:
        if s == s[::-1]:
            return len(s)
        (pattern, re) = (0, 0)
        exit = {pattern: -1}
        for (i, num) in enumerate(s):
            pattern ^= 1 << int(num)
            if pattern == 0:
                re = i + 1
                continue
            for k in range(10):
                new_p = pattern ^ 1 << k
                re = max(re, i - exit.get(new_p, i))
            re = max(re, i - exit.get(pattern, i))
            exit.setdefault(pattern, i)
        return re
