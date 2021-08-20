class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            sign = 1
        else:
            sign = -1
        x = abs(x)
        reserve = 0
        while x > 0:
            reminder = x % 10
            reserve = reserve * 10 + reminder
            x = x // 10
        if reserve > 2 ** 31 - 1:
            reserve = 0
        return reserve * sign
