def find_digit(num, nth):
    if nth <= 0:
        return -1
    elif len(str(num)) < nth:
        return 0
    return int(str(num)[::-1][nth - 1])
