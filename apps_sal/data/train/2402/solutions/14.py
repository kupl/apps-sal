class Solution:

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        z = self.spaceindex(s)
        for i in range(0, len(z) - 1):
            word = s[z[i] + 1:z[i + 1]]
            result = result + word[::-1] + ' '
        return result + s[z[len(z) - 1] + 1:len(s)][::-1]

    def spaceindex(self, s):
        result = [-1]
        for i in range(0, len(s)):
            if s[i] == ' ':
                result.append(i)
        return result
