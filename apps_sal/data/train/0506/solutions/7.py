class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip()
        if not str:
            return 0

        sign = -1 if str[0] == '-' else 1
        if str[0] in ['+', '-']:
            str = str[1:]

        i, res = 0, 0
        while i < len(str) and str[i].isdigit():
            res = res * 10 + ord(str[i]) - ord('0')
            i += 1

        return max(-2**31, min(2**31 - 1, sign * res))
