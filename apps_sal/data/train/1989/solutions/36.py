class Solution:

    def longestAwesome(self, s: str) -> int:
        s = [ord(x) - ord('0') for x in s]
        ans = 0
        m = [None] * 1024
        m[0] = -1
        y = 0
        for (i, x) in enumerate(s):
            y ^= 1 << x
            for j in range(11):
                p = y ^ 1 << j & 1023
                if m[p] != None:
                    ans = max(ans, i - m[p])
            if m[p] == None:
                m[y] = i
        return ans
