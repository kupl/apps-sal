class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        words = list(s.split(' '))
        for word in words:
            for i in range(len(word)):
                res += word[len(word) - i - 1]
            res += ' '
        return res.strip()
