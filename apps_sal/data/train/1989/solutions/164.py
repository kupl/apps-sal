class Solution:

    def longestAwesome(self, s: str) -> int:
        n = len(s)
        c = 0
        counts = [c]
        for x in s:
            c ^= 1 << ord(x) - ord('0')
            counts.append(c)
        good = {1 << i for i in range(10)}
        good.add(0)
        m = {}
        for (i, c) in enumerate(counts):
            if c not in m:
                m[c] = i
        res = 0
        for i in range(1, n + 1):
            for d in (counts[i] ^ g for g in good):
                if d in m:
                    res = max(res, i - m[d])
        return res
