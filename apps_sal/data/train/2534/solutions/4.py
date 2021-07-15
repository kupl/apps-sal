class Solution:
    def maxScore(self, s: str) -> int:
        l = 0
        r = 0
        ans = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                l+=1
            r = 0
            # print(s[:i], s[i:])
            for j in range(i+1, len(s)):
                if s[j] == '1':
                    r += 1
            # print(l, r)
            ans = max(ans, l+r)
        return ans
