class Solution:

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        d = bin(x ^ y)
        return d.count('1')
