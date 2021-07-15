f = lambda n, p: 0 if n < p else n//p + f(n//p, p)


def factors(n):
    p = 2
    while p*p <= n:
        cnt = 0
        while n % p == 0:
            cnt += 1
            n //= p
        yield p, cnt
        p += 1
    if n != 1:
        yield n, 1

def trailing_zeros(number, base):
    return min(f(number, num) // cnt for num, cnt in factors(base) if cnt != 0)
