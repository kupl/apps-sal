class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # get rid of leading whitespaces
        s = str.lstrip()

        if len(s) == 0:
            return 0
        # get integer as far as possible
        if s[0] not in ['+', '-']:
            sign = 1
            i = 0
            while i < len(s) and s[i].isdigit():
                i += 1
            int_as_str = s[:i]
        else:
            sign = 1 if s[0] == '+' else -1
            i = 1
            while i < len(s) and s[i].isdigit():
                i += 1
            int_as_str = s[1:i]

        # convert to integer
        if len(int_as_str) == 0:
            return 0

        return max(-2**31, min(sign * int(int_as_str), 2**31 - 1))
