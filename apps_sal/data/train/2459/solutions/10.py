class Solution:

    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        hexKey = '0123456789abcdef'
        ans = ''
        for _ in range(8):
            ans = hexKey[num & 15] + ans
            num >>= 4
        return ans.lstrip('0')
