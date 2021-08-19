class Solution:
    def longestAwesome(self, s: str) -> int:
        n = len(s)
        ans = 0
        d = {0: -1}
        rolling = 0
        for i, v in enumerate(s):  # pay attention to i
            rolling ^= 1 << int(v)
            for x in range(10):
                diff = rolling ^ (1 << x)
                if diff in d:
                    ans = max(ans, i - d[diff])
            if rolling in d:
                ans = max(ans, i - d[rolling])
            else:
                d[rolling] = i
        return ans
