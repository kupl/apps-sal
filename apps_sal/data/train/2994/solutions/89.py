def find_digit(num, nth):
    if nth > len(str(num)):
        return 0
    elif nth <= 0:
        return -1
    return int(str(num)[-nth])
