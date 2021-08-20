class Solution:

    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return False
        s = 1
        for i in range(2, int(num ** 0.5 + 1)):
            if num % i == 0:
                s += i
                s += num // i
        return s == num
