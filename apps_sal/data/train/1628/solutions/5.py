def proper_fractions(n):
    if n < 3:
        return n - 1
    s, t, i = [], 1, 2
    while True:
        while n % i == 0:
            t, s, n = t * (i if i in s else i - 1), s + [i], n // i
        if i * i > n:
            return t * (n - 1) if n > 1 else t
        i += 1
