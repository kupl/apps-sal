class Solution:

    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while True:
            if num / i < i:
                return False
            elif num / i == i:
                return True
            else:
                i += 1
