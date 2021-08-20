class Solution:

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = []
        while n > 0:
            n -= 1
            tmp = n % 26
            n = int(n / 26)
            ret.append(chr(ord('A') + tmp))
        return ''.join(reversed(ret))
