def totient(n):
    if type(n) is not int or n < 0:
        return 0
    tot = 1
    p = 2
    while n > 1 and p * p <= n:
        k = 0
        while n > 0 and n % p == 0:
            k += 1
            n //= p
        if k > 0:
            tot *= p ** (k - 1) * (p - 1)
        p += 1
    if n > 1:
        tot *= (n - 1)
    return tot
