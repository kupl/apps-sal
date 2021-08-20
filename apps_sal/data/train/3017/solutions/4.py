def rocks(n):
    (r, p, i) = (0, 1, 1)
    while p * 9 < n:
        r += 9 * p * i
        n -= 9 * p
        p *= 10
        i += 1
    return r + n * i
