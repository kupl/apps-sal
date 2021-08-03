class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while len(str(num)) > 1:
            newNum = 0
            while num > 0:
                newNum += num % 10
                num = num // 10
            num = newNum
        return num
