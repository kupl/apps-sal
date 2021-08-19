class Solution:

    def longestAwesome(self, s: str) -> int:
        m = [100000.0 for i in range(1024)]
        m[0] = -1
        es = [1 << i for i in range(10)]
        current = 0
        res = 1
        for (i, c) in enumerate(s):
            n = ord(c) - ord('0')
            current = 1 << n ^ current
            if current == 0:
                res = i + 1
            else:
                for e in es:
                    res = max(res, i - m[current ^ e])
            m[current] = min(m[current], i)
        return res
