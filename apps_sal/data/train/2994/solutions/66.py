def find_digit(num, nth):
    if nth <= 0:
        return -1

    else:
        num = abs(num)
        if nth > len(str(num)):
            return 0
        else:
            return int(str(num)[len(str(num)) - nth])
