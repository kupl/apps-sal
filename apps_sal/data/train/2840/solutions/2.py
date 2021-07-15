def withdraw(n):
    b50 = int(n % 20 == 10)
    b100, b20 = divmod((n - 50 * b50) // 20, 5)
    return [b100, b50, b20]
