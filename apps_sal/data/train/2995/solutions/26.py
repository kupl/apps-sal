def sum_mul(n, m):
    return sum([num for num in range(0, m, n)]) if m > 0 and n > 0 else "INVALID"
