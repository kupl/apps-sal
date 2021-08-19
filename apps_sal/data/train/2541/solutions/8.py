class Solution:

    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        target = 1
        while target < num:
            target *= 4
            if target == num:
                return True
        return False
