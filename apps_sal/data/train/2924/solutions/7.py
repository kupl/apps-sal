def are_coprime(n, m):
    return prime_factors(n) & prime_factors(m) == {1}


def prime_factors(n):
    factors = [1]
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d * d > n:
            if n > 1:
                factors.append(n)
            break
    return set(factors)
