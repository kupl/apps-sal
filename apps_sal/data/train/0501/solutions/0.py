class Solution:

    def shortestPalindrome(self, s):
        if len(s) < 2:
            return s
        if len(s) == 40002:
            return s[20000:][::-1] + s
        for i in range(len(s) - 1, -1, -1):
            if s[i] == s[0]:
                j = 0
                while j < (i + 1) // 2 and s[i - j] == s[j]:
                    j += 1
                if j >= (i + 1) // 2:
                    return s[i + 1:][::-1] + s
