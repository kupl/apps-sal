from fractions import gcd

def are_coprime(a, b):
    return gcd(a, b) == 1
