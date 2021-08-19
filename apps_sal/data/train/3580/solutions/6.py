def get_positions(n):
    n %= 27
    return (n % 3, n // 3 % 3, n // 9)
