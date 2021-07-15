from fractions import gcd

def relatively_prime (n, l):
    return [i for i in l if gcd(i,n) == 1]
