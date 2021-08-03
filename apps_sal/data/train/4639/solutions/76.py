def power_of_two(x):
    exp = 0
    while (x > 2**exp):
        exp += 1
    return 2**exp == x
