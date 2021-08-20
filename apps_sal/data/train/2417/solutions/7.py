class Solution:

    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        minus = True if num < 0 else False
        num = abs(num)
        s = ''
        while num >= 7:
            s += str(num % 7)
            num //= 7
        s += str(num)
        return minus * '-' + s[::-1]
