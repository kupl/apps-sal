def is_divisible(n, x, y):
    if x != 0 and y != 0:
        if n % x == n % y == 0:
            return True
        else:
            return False
    return False
