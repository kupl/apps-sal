def find_digit(num, nth):
    if nth <= 0:
        return -1

    if num < 0:
        num = num * -1

    if len(str(num)) < nth:
        return 0

    return int(str(num)[::-1][nth - 1])
