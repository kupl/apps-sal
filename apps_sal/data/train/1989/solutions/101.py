class Solution:
    def longestAwesome(self, s: str) -> int:
        n = len(s)
        m, seen, ans = 0, [-1] + [n] * 1024, 1
        for i, x in enumerate(s):
            m ^= 1 << int(x)
            for d in range(10):
                ans = max(ans, i - seen[m ^ (1 << d)])
            ans = max(ans, i - seen[m])
            seen[m] = min(seen[m], i)
        return ans
