class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = 0
        for i in range(num):
            x += 1 + 2 * i
            if x == num:
                return True
            if x > num:
                return False
        return False
