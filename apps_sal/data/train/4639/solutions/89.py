def power_of_two(x):
    y = 1
    while x >= y:
        if x == y:
            return True
        y = 2 * y
    return False
