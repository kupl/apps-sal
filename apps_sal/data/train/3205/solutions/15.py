def is_divisible(n, x, y):
    if not n % x:
        if not n % y:
            return True

    return False
