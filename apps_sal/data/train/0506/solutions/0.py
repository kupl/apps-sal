class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        base = "0123456789"
        plus = "+"
        minus = "-"
        sum = 0
        flag = 1
        bit = 0
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        if not str:
            return 0

        if len(str) == 0:
            return 0

        for letter in str.strip():
            if letter in plus:
                if bit == 0:
                    bit = 1
                    continue
                else:
                    break
            elif letter in minus:
                if bit == 0:
                    bit = 1
                    flag = -1
                    continue
                else:
                    break
            elif letter not in base:
                break
            else:
                sum *= 10
                sum += int(letter)

        sum *= flag

        if(sum > INT_MAX):
            return INT_MAX

        if(sum < INT_MIN):
            return INT_MIN

        return sum
