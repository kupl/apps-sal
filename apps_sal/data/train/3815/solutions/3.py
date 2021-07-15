from fractions import gcd 
def coprimes(n): return [a for a in range(1, n) if gcd(n,a) == 1]
