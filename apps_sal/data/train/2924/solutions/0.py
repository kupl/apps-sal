from fractions import gcd

def are_coprime(n, m):
  return gcd(n, m) == 1
