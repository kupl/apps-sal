def divisors(n):
    z = 0
    i = 1
    while i <= n:
        if n % i == 0:
            z += 1
        i += 1
    return z
