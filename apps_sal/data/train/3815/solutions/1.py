from fractions import gcd
def coprimes(n):
    return [i for i in range(n) if gcd(i,n)==1]
