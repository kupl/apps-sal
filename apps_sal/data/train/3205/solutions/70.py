def is_divisible(n, x, y):
    if n % x == 0 and n % y == 0:
        return True
    elif n % x != 0 or n % y != 0:
        return False
