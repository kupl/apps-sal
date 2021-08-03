def primes(n):
    primfac = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac


def mult_primefactor_sum(a, b):
    l = []
    for i in range(a, b + 1):
        factors = primes(i)
        if i > sum(factors) and not i % sum(factors):
            l.append(i)
    return l
