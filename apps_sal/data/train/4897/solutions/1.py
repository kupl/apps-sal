def binary_gcd(x, y):
    import math
    return bin(math.gcd(x, y)).count('1')
