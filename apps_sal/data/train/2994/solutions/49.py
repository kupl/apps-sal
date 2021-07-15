def find_digit(num, nth):
    if nth > len(str(num).replace("-", "")):
        return 0
    if nth <= 0:
        return -1
    else:
        return int(str(num)[::-1][nth-1])

