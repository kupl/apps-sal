from fractions import gcd

def coprimes(n):
  return [i for i in range(1,n+1) if gcd(n,i)==1]
