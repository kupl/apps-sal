"""NOTE: This is NOT an efficient solution, it's just a solution using Python's gcd function"""
from fractions import gcd
'Imports greatest common divisor (gcd)'
'gcd has been moved to the math module in Python 3.5,\nso you should use: from math import gcd'


def is_divisible(n, x, y):
    """Computes the least common multiple (lcm) -> 
    https://en.wikipedia.org/wiki/Least_common_multiple#Computing_the_least_common_multiple"""
    lcm = x * y / gcd(x, y)
    'if x divides n, and y divides n, so lcm(x,y) also divides n'
    return n % lcm == 0
