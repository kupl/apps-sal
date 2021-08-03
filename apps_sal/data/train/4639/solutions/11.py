def power_of_two(x):
    if x == 0:
        return False
    elif x & x - 1 != 0:
        return False
    else:
        return True
