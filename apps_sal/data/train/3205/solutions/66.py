def is_divisible(n, x, y):
    return True if (n / x).is_integer() == True and (n / y).is_integer() == True else False
