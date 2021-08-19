class Solution:

    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) < len(num2):
            (num1, num2) = (num2, num1)
        addon = 0
        res = ''
        l = len(num2)
        for i in range(l):
            s = ord(num2[l - i - 1]) + ord(num1[len(num1) - i - 1]) - 2 * ord('0') + addon
            addon = s // 10
            res = chr(s % 10 + ord('0')) + res
        for i in range(l, len(num1)):
            s = ord(num1[len(num1) - i - 1]) - ord('0') + addon
            addon = s // 10
            res = chr(s % 10 + ord('0')) + res
        if addon > 0:
            res = '1' + res
        return res
