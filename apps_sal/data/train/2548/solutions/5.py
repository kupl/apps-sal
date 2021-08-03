class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        if num == 1:
            return True
        while num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
            if num % 2 == 0:
                num /= 2
            elif num % 3 == 0:
                num /= 3
            else:
                num /= 5
            if num == 1:
                return True
        return False
