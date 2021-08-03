def is_divisible(n, x, y):
    if n < 1 or x < 1 or y < 1:
        return False
    else:
        if (n % x == 0) and (n % y == 0):
            return True
        else:
            return False
