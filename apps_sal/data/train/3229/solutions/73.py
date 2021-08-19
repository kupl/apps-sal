"""import math
def am_i_wilson(n):
    if n > 0:
        x = (math.factorial(n - 1) + 1) / (n**2)
        return True if x == int(x) else False
    else: return False"""


def am_i_wilson(n):
    return True if n in (5, 13, 563) else False
