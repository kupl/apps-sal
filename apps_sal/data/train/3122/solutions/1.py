def chess_triangle(n, m):
    if n > m:
        n, m = m, n
    if m <= 2 or n < 2:
        return 0
    elif n == 2:
        return (m * 2 - 5) * 8
    else:
        return (((2 * n - 4) * (2 * n - 4) - 1) + ((m - n) * 4 * (n - 2))) * 16
