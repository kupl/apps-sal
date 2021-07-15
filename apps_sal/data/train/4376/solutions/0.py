def count_pal(n):
    # No recursion; direct calculation:
    return [9 * 10**((n-1) // 2), 10**(n // 2) * (13 - 9 * (-1)**n) // 2 - 2]
