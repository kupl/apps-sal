import math
import sys
sys.float_info.max


def am_i_wilson(n):
    print(n)
    if n <= 1:
        return False
    if n > 1000:
        if n % 2 == 0:
            return False
        else:
            return False

    def factorial(a):
        if a <= 1:
            return 1
        else:
            return a * factorial(a - 1)
        result = 1
        for i in range(2, a + 1):
            result *= i
        return result
    print('got here')
    num = (math.factorial(n - 1) + 1) % (n * n)
    return num == 0
