def count_pal(n):
    total = 0
    for i in range(n):
        n_digit = 9 * 10 ** (i // 2)
        total += n_digit
    return [n_digit, total]
