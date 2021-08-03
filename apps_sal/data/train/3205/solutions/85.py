def is_divisible(n, x, y):
    print(n, x, y)
    return True if (n / x) % 1 + (n / y) % 1 == 0 else False
