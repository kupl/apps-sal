def is_divisible(n, x, y):
    a = n / x
    b = n / y
    if a == int(a) and b == int(b):
        return True
    else:
        return False
