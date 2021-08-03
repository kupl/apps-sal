class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        str = str.strip()
        if str == '':
            return 0
        str = str.split()[0]

        flag = True
        if str[0] == '+':
            flag = True
            str = str[1:]
        elif str[0] == '-':
            flag = False
            str = str[1:]

        if str == '' or str[0] not in "0123456789":
            return 0
        s = ''
        for ch in str:
            if ch in "0123456789":
                s += ch
            else:
                break
        try:
            result = int(s)
        except:
            return 0
        else:
            if not flag:
                result = -result
        if result > 2147483647:
            result = 2147483647
        elif result < -2147483648:
            result = -2147483648
        return result
