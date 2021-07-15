from math import gcd; is_divisible = lambda n, x, y: not n%(x*y//(gcd(x, y)))
