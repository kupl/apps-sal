def power_of_two(x):
    if x == 0:
        return False
    elif x == 1:
        return True
    else:
        return x % 8 == 0
