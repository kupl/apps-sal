class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = 0
        while num >= 10:
            num, rem = divmod(num, 10)
            num += rem
        return num
