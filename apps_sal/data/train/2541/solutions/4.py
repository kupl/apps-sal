class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num != 0 and not num & (num - 1) and len(bin(num)) % 2 == 1
