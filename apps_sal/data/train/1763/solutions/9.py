def insane_inc_or_dec(n):
    modulo = 12345787
    a, b, k = n + 1, 1, 9
    for r in range(2, k + 1):
        a *= n + r
        b *= r
    binomial = a // b  # is (n+k)-choose-k with k=9
    return (binomial + binomial * (n + 10) // 10 - 10 * n - 2) % modulo
