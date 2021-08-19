class Solution:

    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        mp = '0123456789abcdef'
        ans = ''
        for i in range(8):
            n = num % 16
            c = mp[n]
            ans = c + ans
            num = num >> 4
        return ans.lstrip('0')
