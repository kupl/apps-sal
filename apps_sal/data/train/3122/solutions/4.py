def chess_triangle(n, m):
    if n < 2 or m < 2 or (n == 2 and m == 2):
        return 0
    else:
        a = (max((n - 1) * (m - 2), 0) + max((n - 2) * (m - 1), 0))
        b = (max((n - 1) * (m - 3), 0) + max((n - 3) * (m - 1), 0))
        c = (max((n - 2) * (m - 2) * 2, 0))
        d = (max((n - 2) * (m - 3), 0) + max((n - 3) * (m - 2), 0))
        return (a + b + c + d) * 8
