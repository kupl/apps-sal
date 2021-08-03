def power_of_two(x):
    result = 0
    i = 0
    while result < x:
        result = 2 ** i
        i += 1
        if result != x:
            continue
        if result == x:
            return True
    return False
