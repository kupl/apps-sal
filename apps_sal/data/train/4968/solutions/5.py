def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def relatively_prime(n, l):
    return [x for x in l if gcd(n, x) == 1]
