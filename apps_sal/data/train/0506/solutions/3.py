class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        str = str.strip()
        if not str:
            return 0
        sign = 1
        if str[0] in ("+", "-"):
            if str[0] == "-":
                sign = -1
            str = str[1:]
        if not str:
            return 0
        if not str[0].isdigit():
            return 0
        for ind, val in enumerate(str):
            if not val.isdigit():
                str = str[:ind]
                break
        #sum = 0
        #scale = 1
        # for element in str[::-1]:
        #    sum += scale * int (element)
        #    scale *= 10
        sum = int(str)

        result = sign * sum
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
        return result
