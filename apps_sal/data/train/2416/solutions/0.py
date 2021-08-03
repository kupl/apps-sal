class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n = num**0.5
        if n == int(n):
            return True
        else:
            return False
