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

    def find(self, text, pattern):
        ans = []
        t = self.prefixTable(pattern)
        i = j = 0
        while i < len(text):
            if text[i] == pattern[j]:
                i += 1
                j += 1

            if j == len(pattern):
                ans.append(i - len(pattern))
                j = t[j - 1]

            elif i < len(text) and text[i] != pattern[j]:
                if j > 0:
                    j = t[j - 1]
                else:
                    i += 1
        return ans

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        ans = self.find(haystack, needle)
        return ans[0] if ans else -1
