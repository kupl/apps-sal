def is_divisible(n, x, y):
    if n % x != 0 and n % y != 0:
        return False
    if n % x != 0 or n % y != 0:
        return False
    elif n % x == 0 and n % y == 0:
        return True


is_divisible(3, 3, 4)
