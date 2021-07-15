def power_of_two(x):
    return x and not bool(x & (x-1))
