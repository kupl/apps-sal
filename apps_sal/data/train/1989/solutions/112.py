class Solution:
    def longestAwesome(self, s):
        d = {0: -1}
        t = 0
        ans = 0
        for i in range(len(s)):
            num = int(s[i])
            # update tuple
            t ^= 1 << num
            if t not in d:
                d[t] = i
                for m in range(10):
                    temp = t ^ (1 << m)
                    if temp in d:
                        ans = max(ans, i - d[temp])
            else:
                ans = max(ans, i - d[t])
                for m in range(10):
                    temp = t ^ (1 << m)
                    if temp in d:
                        ans = max(ans, i - d[temp])

        return ans
