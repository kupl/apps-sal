class Solution:

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        else:
            return self.addDigits(sum([int(x) for x in str(num)]))
