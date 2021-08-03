def find_last(n, m):
    num = 0
    for i in range(2, n + 1):
        num = (num + m) % i
    return num + 1, n * (n + 1) + m * (m - 2) - n * m
