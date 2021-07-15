import math

def multiply(n):
    return n * 5**(int(math.log10(abs(n)))+1) if n else 0
