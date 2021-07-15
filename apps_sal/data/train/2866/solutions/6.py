def mobius(n):
    d, k = 2, 0
    while d * d <= n:
        if n % d == 0:
            n //= d
            if n % d == 0:
                return 0
            k += 1
        d += 1
    if n > 1:
        k += 1
    return 1 - k % 2 * 2
