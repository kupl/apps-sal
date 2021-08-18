class Solution:
    def longestAwesome(self, s: str) -> int:
        if len(s) == 0:
            return 0

        max_len = 1
        p = [0] * len(s)
        seen = {0: -1}
        for i in range(0, len(s)):
            d = ord(s[i]) - ord('0')
            p[i] = (1 << d) ^ p[i - 1]

            for od in range(10):
                x = p[i] | (1 << od)
                if x in seen:
                    max_len = max(max_len, i - seen[x])
                y = p[i] & (~(1 << od))
                if y in seen:
                    max_len = max(max_len, i - seen[y])

            if p[i] not in seen:
                seen[p[i]] = i

        return max_len
