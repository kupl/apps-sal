class Solution:

    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """

        def decTo7(n):
            new = ''
            while n / 7 != 0:
                new += str(n % 7)
                n //= 7
            if new == '':
                return '0'
            return new[::-1]
        if num >= 0:
            return decTo7(num)
        else:
            return '-' + decTo7(abs(num))
