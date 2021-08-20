class Solution:

    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        if num < 0:
            num = num + 2 ** 32
        mapping = '0123456789abcdef'
        output = ''
        while num > 0:
            print(num)
            remainder = num % 16
            output = mapping[remainder] + output
            num = math.floor(num / 16)
        return output
