def transform(A, x):
    c, i, f, r = 1, x, 0, None
    for n in sorted(A):
        while i <= n:
            c *= i
            c //= i-x or x
            i += 1
            f += c
        if r is None: r = f
        else: r ^= f
    return r
