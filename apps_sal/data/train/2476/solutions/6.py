class Solution:

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num // 10 > 0:
            rlt = 0
            while num > 0:
                rlt += num % 10
                num //= 10
            num = rlt
        return num
