class Solution:

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x is 0:
            return 0
        ori_str = str(x)
        answer = 0
        if ori_str[0] is '-':
            answer = -1 * int(ori_str[:0:-1].lstrip('0'))
        else:
            answer = int(ori_str[::-1].lstrip('0'))
        if answer >= 2 ** 31 or answer < -2 ** 31:
            return 0
        else:
            return answer
