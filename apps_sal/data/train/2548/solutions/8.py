class Solution:

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        elif num == 1:
            return True
        for factor in (5, 3, 2):
            while num % factor == 0:
                num = num / factor
                print(num)
        return int(num) == 1
