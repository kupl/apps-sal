class Solution:

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x > 0:
            sign = 1
        else:
            sign = -1
            x = 0 - x
        bits = []
        for i in range(10):
            bits.append(x % 10)
            x = x // 10
        print(bits)
        left_i = 0
        right_i = 9
        for i in range(10):
            if bits[i] == 0:
                left_i = left_i + 1
            else:
                break
        for i in range(9, -1, -1):
            if bits[i] == 0:
                right_i = right_i - 1
            else:
                break
        print(left_i, right_i)
        factor = 1
        result = 0
        for i in range(right_i, left_i - 1, -1):
            result = result + factor * bits[i]
            factor = factor * 10
        result = result * sign
        if result > 2147483647 or result < -2147483648:
            return 0
        else:
            return result
