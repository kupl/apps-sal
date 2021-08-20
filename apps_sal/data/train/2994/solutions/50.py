def find_digit(n, m):
    return int(f'{n:099d}'[::-1][m - 1]) if m > 0 else -1
