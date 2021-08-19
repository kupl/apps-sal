class Solution:

    def longestAwesome(self, s: str) -> int:
        cur = ans = 0
        m = {}
        for (i, c) in enumerate(s):
            cur ^= 1 << int(c)
            if cur == 0:
                ans = max(ans, i + 1)
            elif cur == 2 ** int(math.log(cur, 2)):
                ans = max(ans, i + 1)
            else:
                for j in range(10):
                    new = cur ^ 1 << j
                    if new in m:
                        ans = max(i - m[new], ans)
            if cur not in m:
                m[cur] = i
        return ans
