class Solution:

    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        middle = num // 2 + 1
        for i in range(0, middle + 1):
            if i * i == num:
                return True
            if i * i > num:
                return False
