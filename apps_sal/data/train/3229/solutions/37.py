import math
def am_i_wilson(num):
    if num < 2 or num > 563 or not all(num % i for i in range(2, num)):
        return False
    return (math.factorial(num - 1) + 1) % (num ** 2) == 0
