import math

def multiply(n):
    if n == 0:
        digits = 1
    else:
        digits = int(math.log10(abs(n)))+1
    return n * 5 ** digits
