def power_of_two(x):
    if x == 0:
        return False
    else:
        return x & -x == x
