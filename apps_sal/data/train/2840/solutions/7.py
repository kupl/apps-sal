def withdraw(n):
    b50 = int(n % 20 == 10)
    (b100, n) = divmod(n - 50 * b50, 100)
    return [b100, b50, n // 20]
