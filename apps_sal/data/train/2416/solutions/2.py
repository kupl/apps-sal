class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        start = 1
        while num > 0:
            num = num - start
            start = start + 2

        if num == 0:
            return True

        return False
