def power_of_two(num):
    if num == 0:
        return False
    elif num & num - 1 != 0:
        return False
    else:
        return True
