class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        mp = '0123456789abcdef'  # like a map
        ans = ''
        for i in range(8):
            n = num % 16       # or n=num & 15, this means num & 1111b
            c = mp[n]          # get the hex char
            ans = c + ans
            num = num >> 4  # num的二进制编码右移4位
        return ans.lstrip('0')  # strip leading zeroes
