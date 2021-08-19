def is_divisible(n, x, y):
    n = int(n)
    x = int(x)
    y = int(y)
    if n % x != 0 or n % y != 0:
        return False
    else:
        return True
