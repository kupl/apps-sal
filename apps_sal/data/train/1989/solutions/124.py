class Solution:
    def longestAwesome(self, s: str) -> int:

        seen = {0: -1}
        max_len = 0

        n = 0
        for i in range(len(s)):
            digit = int(s[i])
            n = n ^ (1 << digit)

            if n in seen:
                max_len = max(max_len, i - seen[n])

            for start in range(10):
                m = n ^ (1 << start)
                if m in seen:
                    max_len = max(max_len, i - seen[m])

            if n not in seen:
                seen[n] = i

        return max_len
