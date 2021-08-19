class Solution:

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_x = str(x)
        n = len(str_x)
        if str_x[0] != '-':
            y = int(str_x[::-1])
        else:
            y = -int(str_x[:0:-1])
        return y * (y.bit_length() < 32)
