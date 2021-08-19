class Solution:

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = x ** 0.5
        return math.floor(a)
