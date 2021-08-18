class Solution:
    def prefixTable(self, s):
        t = [0 for _ in s]
        j = 0
        i = 1
        while i < len(s):
            if j == 0 and s[i] != s[j]:
                t[i] = 0
                i += 1
            elif s[i] == s[j]:
                t[i] = j + 1
                i += 1
                j += 1
            elif j > 0 and s[j] != s[i]:
                j = t[j - 1]
        return t

    def shortestPalindrome(self, s):
        k = s + "
        t = self.prefixTable(k)
        l = t[-1]
        return s[l:][::-1] + s
