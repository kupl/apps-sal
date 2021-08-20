class Solution:

    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            num = 2 ** 32 - 1 - ~num
        if num == 0:
            return '0'
        s = ''
        dic = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        for i in range(8, -1, -1):
            if int(num / 16 ** i) > 0:
                if int(num / 16 ** i) < 10:
                    s = s + str(int(num / 16 ** i))
                else:
                    s = s + dic[int(num / 16 ** i)]
                num = num - int(num / 16 ** i) * 16 ** i
            elif len(s) > 0:
                s = s + '0'
        return s
