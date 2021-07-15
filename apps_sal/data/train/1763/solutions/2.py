def insane_inc_or_dec(m):
    num = den = 1
    for i in range(1, 11):
        num *= m + i + i * (i >= 10)
        den *= i
    return (num // den - 10 * m - 2) % 12345787
