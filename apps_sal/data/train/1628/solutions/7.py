def unique_prime_factors(n):
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors


def proper_fractions(n):
    if n == 1:
        return 0
    output = n
    for p in unique_prime_factors(n):
        output //= p
        output *= (p - 1)
    return output
