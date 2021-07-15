def power_of_two(x):
    return not(x & (x-1)) if x != 0 else False
