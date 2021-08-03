def find_digit(num, nth):
    if nth <= 0:
        return -1
    elif nth <= len(str(num)):
        return int(str(num)[::-1][nth - 1])
    else:
        return 0
