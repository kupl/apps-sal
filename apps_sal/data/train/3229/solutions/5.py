"""from math import factorial, sqrt

def prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))

def am_i_wilson(n):
    if not prime(n):
        return False
    elif:
        n == 0:
            return False
    else:
        square = n ** 2
        val = (factorial(n) + 1) / square
        if val > 0:
            return True
        else:
            return False
"""

def am_i_wilson(n):
    return n in [5, 13, 563]
