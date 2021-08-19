class Solution:

    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        p = 1
        n = 1
        while n < num:
            n = 2 ** (p - 1) * (2 ** p - 1)
            if n == num:
                return True
            p += 1
        return False
