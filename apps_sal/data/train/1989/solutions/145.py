class Solution:
    def longestAwesome(self, s: str) -> int:
        s = [int(c) for c in s]
        seen = {0: -1} #we've seen the case all even, at the beginning
        valid = [0] + [1 << i for i in range(10)]
        totSum = 0
        res = 0
        N = len(s)
        for i in range(N):
            totSum ^= 1 << s[i]
            for y in valid:
                needed = totSum ^ y
                if needed in seen:
                    res = max(res, i - seen[needed])
            if totSum not in seen:
                seen[totSum] = i
        return res
