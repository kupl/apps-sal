class Solution:
    def longestAwesome(self, s: str) -> int:
        # TC: O(N), SC: O(1), prefix + bitmask
        n = len(s)
        # bitmask on each digits is odd or even
        # at most one odd is ok => at most one 1s in bitmask
        m, seen, ans = 0, [-1] + [n] * 1024, 1
        for i, x in enumerate(s):
            m ^= 1 << int(x)
            for d in range(10):
                ans = max(ans, i - seen[m ^ (1 << d)])
            ans = max(ans, i - seen[m])
            seen[m] = min(seen[m], i)
        return ans
