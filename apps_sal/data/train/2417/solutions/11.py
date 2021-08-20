class Solution:

    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            negative = '-'
            num *= -1
        else:
            negative = ''
        p = 1
        while p <= num:
            p *= 7
        p = p // 7
        digits = []
        while p > 1:
            digits.append(num // p)
            num = num % p
            p = p // 7
        digits.append(num)
        result = negative + ''.join([str(x) for x in digits])
        return result
