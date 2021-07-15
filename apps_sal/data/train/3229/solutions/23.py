import math

def am_i_wilson(n):
    return (math.factorial(n-1) + 1) % (n**2) == 0 if n > 1 and n < 100000 else False
