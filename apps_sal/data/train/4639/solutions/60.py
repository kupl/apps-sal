def power_of_two(x):
    for i in range(101):
        if 2 ** i == x:
            return True
    return False
