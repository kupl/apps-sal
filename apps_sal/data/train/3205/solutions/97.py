def is_divisible(n, x, y):
    if (n / x).is_integer() == False:
        return False
    if (n / y).is_integer() == False:
        return False
    else:
        return True
