def is_divisible(n, x, y):
    num = int(n)
    numx = int(x)
    numy = int(y)
    if num % x == 0 and num % y == 0:
        return True
    else:
        return False
