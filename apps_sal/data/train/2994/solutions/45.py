def find_digit(num, nth):
    if nth <= 0:
        return -1
    elif nth > abs(num) or nth > len(str(abs(num))):
        return 0
    else:
        return int(str(abs(num))[-nth])
