class Solution:

    def longestAwesome(self, s: str) -> int:
        ps = {}
        mask = 0
        best = 0
        ps[mask] = -1
        for (i, c) in enumerate(s):
            d = int(c)
            mask ^= 1 << d
            if mask in ps:
                best = max(best, i - ps[mask])
            else:
                ps[mask] = i
            for k in range(10):
                if mask ^ 1 << k in ps:
                    best = max(best, i - ps[mask ^ 1 << k])
        return best
