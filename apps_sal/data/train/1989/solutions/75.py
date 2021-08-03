class Solution:
    def longestAwesome(self, s: str) -> int:

        M = {0: -1}
        ans = 0
        code = 0

        D = [(1 << d) for d in range(10)]

        for i, c in enumerate(s):
            code = code ^ (1 << (ord(c) - ord('0')))

            if code in M:
                ans = max(ans, i - M[code])

            for dc in D:
                dcode = code ^ dc
                if dcode in M:
                    ans = max(ans, i - M[dcode])

            if code not in M:
                M[code] = i

        return ans
