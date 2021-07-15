def champernowne_digit(n):
    if not type(n) is int or n < 1:
        return float("NaN")
    i, l = 1, 11
    while l <= n:
        i, l = i + 1, l + 9 * (i + 1) * 10**i
    return ((n - l) // (i * 10**(i - 1 - (n - l) % i))) % 10

champernowneDigit = champernowne_digit

