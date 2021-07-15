import math
def am_i_wilson(n):
    if n < 2 or not all(n % i for i in range(2, n)):
        return False
    return (math.factorial(n - 1) + 1) % (n ** 2) == 0
