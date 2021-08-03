class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s.split())
        a = ""
        for i in range(len(s)):
            if i + 1 < len(s):
                s[i] = list(s[i])
                start = 0
                end = len(s[i]) - 1
                while start < end:
                    temp = s[i][start]
                    s[i][start] = s[i][end]
                    s[i][end] = temp
                    start += 1
                    end -= 1
                s[i] = "".join(s[i])
                a += s[i]
                a += " "
            else:
                s[i] = list(s[i])
                start = 0
                end = len(s[i]) - 1
                while start < end:
                    temp = s[i][start]
                    s[i][start] = s[i][end]
                    s[i][end] = temp
                    start += 1
                    end -= 1
                s[i] = "".join(s[i])
                a += s[i]
        return a
