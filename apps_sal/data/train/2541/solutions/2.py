class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        return (num - 1) & num == 0 and num & 0x55555555 != 0
