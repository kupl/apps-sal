def chess_triangle(n, m):
    x23 = max(0, n - 1) * max(0, m - 2) * 8
    x32 = max(0, n - 2) * max(0, m - 1) * 8
    x24 = max(0, n - 1) * max(0, m - 3) * 8
    x42 = max(0, n - 3) * max(0, m - 1) * 8
    x34 = max(0, n - 2) * max(0, m - 3) * 8
    x43 = max(0, n - 3) * max(0, m - 2) * 8
    x33 = max(0, n - 2) * max(0, m - 2) * 16
    return x23 + x32 + x24 + x42 + x34 + x43 + x33
