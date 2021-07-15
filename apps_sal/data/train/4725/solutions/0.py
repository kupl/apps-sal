def reverse(n):
    m = 0
    while n > 0:
        n, m = n // 10, m * 10 + n % 10
    return m
