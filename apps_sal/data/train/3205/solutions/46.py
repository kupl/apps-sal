def is_divisible(n, x, y):
    if n > 0:
        if n % x == 0 and n % y == 0:
            return True
        else:
            return False
    else:
        print("Inputs should be positive, non-zero digits!")
