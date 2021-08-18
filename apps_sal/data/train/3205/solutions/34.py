def is_divisible(n, x, y):
    ifx = True
    ify = True
    if ((n % x != 0) or (n % y != 0)):
        if ((n % x != 0) and (n % y != 0)):
            ifx = False
            ify = False
        elif (n % x != 0):
            ifx = False
        elif (n % y != 0):
            ify = False

    if ((ifx == False) or (ify == False)):
        return False
    else:
        return True
