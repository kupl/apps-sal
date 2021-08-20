class Solution:

    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        num = num ** 0.5
        if num == int(num):
            return True
        return False
