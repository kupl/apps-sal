from functools import reduce
def f(n):
    facts = factorization(n)
    return mul(power * prime ** (power - 1) for prime, power in facts)

def mul(ar):
    return reduce(lambda x,y:x*y, ar)

def factorization(n):
    result = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            power = 0
            while n % i == 0:
                power += 1
                n /= i
            result.append((i, power))
        i += 1
    if n > 1: result.append((n, 1))
    return result

