class Solution:

    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        return not num & num - 1 and len(bin(num)) % 2 == 1
