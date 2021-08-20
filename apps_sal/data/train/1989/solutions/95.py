class Solution:

    def longestAwesome(self, s):
        d = {(0,) * 10: -1}
        t = (0,) * 10
        ans = 0
        for i in range(len(s)):
            num = int(s[i])
            t = t[:num] + ((t[num] + 1) % 2,) + t[num + 1:]
            if t not in d:
                d[t] = i
                for m in range(10):
                    temp = t[:m] + (1 - t[m],) + t[m + 1:]
                    if temp in d:
                        ans = max(ans, i - d[temp])
            else:
                ans = max(ans, i - d[t])
                for m in range(10):
                    temp = t[:m] + (1 - t[m],) + t[m + 1:]
                    if temp in d:
                        ans = max(ans, i - d[temp])
        return ans
