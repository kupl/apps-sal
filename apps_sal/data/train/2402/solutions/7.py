class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        output = []
        for i in words:
            output += [''.join(reversed(i))]
        return ' '.join(output)
