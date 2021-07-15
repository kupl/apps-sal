def power_of_two(x):
    if x in (0, 1):
        return x
    elif x % 2 == 1:
        return False
    else:
        return power_of_two(x // 2)
