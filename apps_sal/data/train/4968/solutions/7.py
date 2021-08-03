def relatively_prime(n, l):
    from fractions import gcd
    return [i for i in l if gcd(n, i) == 1]
