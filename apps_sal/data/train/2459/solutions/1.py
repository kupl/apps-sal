class Solution:

    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            num = 2 ** 32 + num
        return hex(num)[2:]
