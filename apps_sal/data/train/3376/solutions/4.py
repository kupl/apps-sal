def square_free_part(n):
    if type(n) != int or n <= 0:
        return None
    (r, d) = (1, 2)
    while d * d <= n:
        if n % d == 0:
            while n % d == 0:
                n //= d
            r *= d
        d += 1
    return r * n if n > 1 else r
