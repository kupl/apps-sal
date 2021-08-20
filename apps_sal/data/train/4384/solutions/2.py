def fraction(a, b):
    from math import gcd
    return (a + b) / gcd(a, b)
