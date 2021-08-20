def nth_fib(n):
    n -= 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    (a, b, p, q) = (1, 0, 0, 1)
    while n > 0:
        if n % 2 == 0:
            tp = p
            p = p ** 2 + q ** 2
            q = 2 * tp * q + q ** 2
            n //= 2
        else:
            ta = a
            a = b * q + a * q + a * p
            b = b * p + ta * q
            n -= 1
    return b
