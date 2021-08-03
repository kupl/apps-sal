class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num

        curr_num = num
        total = 0

        while True:
            while curr_num > 0:
                digit = curr_num % 10
                total += digit
                curr_num = curr_num // 10

            if total < 10:
                return total
            else:
                curr_num = total
                total = 0
