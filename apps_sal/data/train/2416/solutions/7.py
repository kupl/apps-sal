class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        n = 100
        n = int(n / 2 + num / 2 / n)
        while n**2 > num:
            n = int(n / 2 + num / 2 / n)
        if n**2 == num:
            return True
        else:
            return False
