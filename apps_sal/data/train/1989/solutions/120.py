class Solution:
    def longestAwesome(self, s: str) -> int:
        h = {}
        ll = len(s)
        m = 0
        maxi = -1
        h[0] = -1
        for i in range(0, len(s)):

            m = m ^ (1 << int(s[i]))

            if m in h:
                maxi = max(maxi, i - h.get(m))
            else:
                h[m] = i

            for l in range(0, 10):
                new_hash = m ^ (1 << l)
                if new_hash in h:
                    maxi = max(maxi, i - h[new_hash])

        return maxi
