from fractions import gcd

coprimes = lambda n: [i for i in range(1, n) if gcd(n, i) == 1]
