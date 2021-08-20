def power_of_two(x):
    while x > 1:
        if x % 2:
            return False
        x //= 2
    return x != 0
