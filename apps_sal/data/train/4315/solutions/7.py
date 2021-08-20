def sum_them(n):
    return (1 << n) - 1 << n - 1 if n > 0 else 0
