def sum_of_n(n):
    sign, n = (1, -1)[n < 0], abs(n)
    return [sign * (i * i + i) / 2 for i in range(n + 1)]
