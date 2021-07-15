from math import factorial

def am_i_wilson(n: int):
    """ Check if given number is a wilson prime. """
    if 563 >= n > 1:
        return not (factorial(n - 1) + 1) % pow(n, 2)
    return False
