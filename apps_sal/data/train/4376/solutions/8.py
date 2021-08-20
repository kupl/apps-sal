def count_pal(n):
    return [10 ** (n - 1 >> 1) * 9, 10 ** (n - 1 >> 1) * (20 - n % 2 * 9) - 2]
