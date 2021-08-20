class Solution:

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp = s.split()
        return ' '.join((i[::-1] for i in tmp))
