class Solution:
    def longestAwesome(self, s: str) -> int:
        if len(s) == 0:
            return 0

        seen = {0: -1}
        max_len = 1
        p = [0] * len(s)
        for i in range(0, len(s)):
            d = ord(s[i]) - ord('0')
            p[i] = (1 << d) ^ p[i - 1]

            if p[i] in seen:
                max_len = max(max_len, i - seen[p[i]])

            for d in range(10):
                x = p[i] | (1 << d)
                if x in seen:
                    max_len = max(max_len, i - seen[x])
                y = p[i] & (~(1 << d))
                if y in seen:
                    max_len = max(max_len, i - seen[y])

            if p[i] not in seen:
                seen[p[i]] = i

        return max_len
