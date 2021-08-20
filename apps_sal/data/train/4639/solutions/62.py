def power_of_two(x):
    i = 0
    while pow(2, i) <= x:
        if pow(2, i) == x:
            return True
        i += 1
    return False
