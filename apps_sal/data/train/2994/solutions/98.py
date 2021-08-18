def find_digit(num, nth):
    if nth > len(str(abs(num))):
        return 0
    elif nth > 0 and abs(num) >= nth:
        y = str(abs(num))
        return int(y[-nth])
    return -1
