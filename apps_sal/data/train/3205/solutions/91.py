def is_divisible(n, x, y):
    return True if (n / x).is_integer() and (n / y).is_integer() > 0 else False
