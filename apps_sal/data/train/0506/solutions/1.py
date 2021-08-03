class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import sys
        str = str.lstrip()
        if not str:
            return 0
        negative = (str[0] == '-')
        str = str.lstrip('')
        if str[0] in ('-', '+'):
            str = str[1:]
        str.lstrip('0')
        result = 0
        for s in str:
            if s.isnumeric():
                result *= 10
                result += int(s)
            else:
                break
        return max(min(result * (-1 if negative else 1), 2147483647), -2147483648)
