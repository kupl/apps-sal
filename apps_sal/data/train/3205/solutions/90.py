def is_divisible(n, x, y):
    return True if not (bool(n % x) or bool(n % y)) else False
