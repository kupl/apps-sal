def is_divisible(n, x, y):
    (num, num1) = (n / y, n / x)
    if num == int(n / y) and num1 == int(n / x):
        return True
    else:
        return False
