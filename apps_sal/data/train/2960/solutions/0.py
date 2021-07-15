from fractions import gcd

def sum_differences_between_products_and_LCMs(pairs):
    return sum(a*b - a*b//gcd(a,b) for a, b in pairs if a and b)
