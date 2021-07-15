def count_odd_pentaFib(n):
    return 2 * (n // 6) + [0, 1, 2, 2, 2, 2][n % 6] - (n >= 2)
