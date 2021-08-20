def is_very_even_number(n):
    while n >= 10:
        (p, n) = (n, 0)
        while p > 0:
            re = p % 10
            n += re
            p //= 10
    return n % 2 == 0
