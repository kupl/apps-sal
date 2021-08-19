class Solution:

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num = num // i
        return num == 1
