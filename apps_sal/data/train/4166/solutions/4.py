def solve(p):
    n = p - 1
    while n % 2 == 0 and pow(10, n, p) == 1:
        n //= 2
    s = pow(10, n, p)
    for p2 in factors_gen(n):
        if pow(10, n // p2, p) == s:
            n //= p2
    return ('%d-sum' if s == 1 else '%d-altsum') % n


def factors_gen(n):
    while n % 2 == 0:
        yield 2
        n //= 2
    k = 3
    while k * k <= n:
        while n % k == 0:
            yield k
            n //= k
        k += 2
    if n > 1:
        yield n
