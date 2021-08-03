class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        sqrt_root = math.sqrt(num)
        if math.floor(sqrt_root) == sqrt_root:
            return int(sqrt_root) & int(sqrt_root - 1) == 0
        return False
