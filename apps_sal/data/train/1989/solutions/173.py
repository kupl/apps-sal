class Solution:
    def longestAwesome(self, s: str) -> int:
        n = len(s)
        seen = {0:-1}
        status = res = 0
        for i, c in enumerate(s):
            status ^= 1 << (ord(c) - ord('0'))
            for a in range(10):
                if status ^ (1 << a) in seen:
                    res = max(res, i - seen[status ^ (1 << a)])
            if status in seen:
                res = max(res, i - seen[status])
            else:
                seen[status] = i
        return res
