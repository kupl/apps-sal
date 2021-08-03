class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if(num < 10):
            return num
        else:
            return self.addDigits(num % 10 + self.addDigits(num // 10))
