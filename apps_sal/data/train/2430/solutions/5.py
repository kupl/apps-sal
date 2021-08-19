class Solution:

    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return '00' not in bin(n) and '11' not in bin(n)
