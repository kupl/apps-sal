class Solution:

    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        a = ''
        n = False
        if num == 0:
            return '0'
        if num < 0:
            num = -num
            n = True
        while num != 0:
            a = str(num % 7) + a
            num //= 7
        if n == True:
            return '-' + a
        return a
