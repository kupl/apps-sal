class Solution(object):
    def toHex(self, num):
        if num == 0:
            return '0'
        if num < 0:
            num = num + 2**32
        hexa = '0123456789abcdef'
        r = ''
        while num:
            r = hexa[num % 16] + r
            num = num // 16
        return r
