class Solution:

    def reverseStr(self, s, k):
        ans = ''
        i = 0
        while i < len(s):
            rev = ''
            j = 0
            while i + j < len(s) and j < k:
                rev += s[i + j]
                j += 1
            i += j
            ans += rev[::-1]
            j = 0
            while i + j < len(s) and j < k:
                ans += s[i + j]
                j += 1
            i += j
        return ans
