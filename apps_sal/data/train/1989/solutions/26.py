class Solution:

    def longestAwesome(self, s: str) -> int:
        d = {0: -1}
        m = b = 0
        for (i, c) in enumerate(s):
            b ^= 1 << int(c)
            m = max(m, i - d.get(b, i - 1))
            h = 1
            for _ in range(10):
                m = max(m, i - d.get(~h & b if h & b else h + b, i - 1))
                h <<= 1
            d.setdefault(b, i)
        return m
