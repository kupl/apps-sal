from functools import reduce
def lcm(*args):
    return reduce(lcms, args) if args else 1

def gcd(a,b):
    """Euclidean Algorithm"""
    return b if a == 0 else gcd(b % a, a)
    
def lcms(a, b):
    return (a*b) // gcd(a,b)
