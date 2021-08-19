class Solution:

    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        i = 1
        while True:
            pow2 = i ** 2
            i += 1
            if pow2 > num:
                return False
            if pow2 == num:
                return True
