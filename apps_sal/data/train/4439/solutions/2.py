def div_num(a, b):
    return "Error" if a > b else min((-divcount(n), n) for n in range(a, b+1))[1]


def divcount(n):
    c = 1 + (n > 1)
    for k in range(2, int(n**0.5) + 1):
        if n % k == 0:
            c += 2 - (k == n // k)
    return c
