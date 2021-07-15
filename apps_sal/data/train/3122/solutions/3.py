def chess_triangle(n, m):
    c = 0
    for i in range(n - 1):
        for j in range(m - 2):
            c += 1 + (i - 1 >= 0) + (i + 3 < n) + (j + 3 < m)
            c += 1 + (i + 1 < n and j - 1 >= 0) + (i + 2 < n) + (i - 2 >= 0)
    for i in range(n - 2):
        for j in range(m - 1):
            c += 1 + (j - 1 >= 0) + (j + 3 < m) + (i + 3 < n)
            c += 1 + (j + 1 < m and i - 1 >= 0) + (j + 2 < m) + (j - 2 >= 0)
    return c * 4
