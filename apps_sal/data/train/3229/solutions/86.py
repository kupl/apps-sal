import math
import sys
sys.float_info.max
# sys.setrecursionlimit(n)


def am_i_wilson(n):
    # sys.setrecursionlimit(100000)
    print(n)
    if n <= 1:
        return False
    if n > 1000:
        if n % 2 == 0:  # even
            return False
        else:  # odd
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
