import math


def is_prime(n):
    if n < 2:
        return False
    if(n in [2, 3]):
        return True
    if(n % 6 not in [1, 5]):
        return False
    for i in range(3, int(math.floor(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True
