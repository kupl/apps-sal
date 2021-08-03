class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ''
        num1 = abs(num)
        while num1:
            ans = str(num1 % 7) + ans
            num1 //= 7

        if num < 0:
            return '-' + ans
        elif num == 0:
            return '0'

        return ans
