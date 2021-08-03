class Solution:
    def longestAwesome(self, s: str) -> int:
        d = {0: -1}
        b = 0
        m = 0
        for i, c in enumerate(s):
            b ^= 1 << int(c)
            if not b or not(b & b - 1):
                m = max(m, i - d.get(b, i - 1), i + 1)
                if not b:
                    h = 1
                    for _ in range(10):
                        m = max(m, i - d.get(h, i - 1))
                        h <<= 1
            else:
                m = max(m, i - d.get(b, i - 1))
                h = 1
                for _ in range(10):
                    if h & b:
                        m = max(m, i - d.get((~h) & b, i - 1))
                    else:
                        m = max(m, i - d.get(h + b, i - 1))
                    h <<= 1
            if b not in d:
                d[b] = i
        return m
