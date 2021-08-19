# checks if n is divisble by x and y
def is_divisible(n, x, y):
    if n % x == 0 and n % y == 0:
        return True
    else:
        return False
