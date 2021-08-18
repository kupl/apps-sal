def power_of_two(x):
    if (x and (x & (x - 1)) == 0):
        return True
    else:
        return False
