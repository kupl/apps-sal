from math import sqrt, factorial


def c(n, m):
    return factorial(n) // (factorial(n - m) * factorial(m))


def factor(n):  # Amount of prime numbers
    factors = {}
    max = int(sqrt(n) + 1)
    f = 2
    while f <= max:
        if n % f == 0:
            factors[f] = 0
            while n % f == 0:
                factors[f] += 1
                n //= f
            max = int(sqrt(n) + 1)
        f += 1
    if n != 1:
        factors[n] = 1
    return factors


def multiply(n, k):
    mul = 1
    for m in factor(n).values():
        mul *= c(m + k - 1, k - 1)
    return mul
