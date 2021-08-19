def is_divisible(n, x, y):
    check = True
    if n % x == 0 and n % y == 0:
        check = True
        return check
    else:
        check = False
        return check
