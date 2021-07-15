def power_of_two(x):
    if x == 0:
        return False
    elif x == 1:
        return True
    elif x % 2 == 0:
        return power_of_two(x // 2)
    else:
        return False
