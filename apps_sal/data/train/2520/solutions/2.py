class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            x = int(str(x)[::-1])
        elif x < 0:
            x = 0 - int(str(abs(x))[::-1])
        if -2 ** 31 < x < 2 ** 31:
            return x
        else:
            return 0
