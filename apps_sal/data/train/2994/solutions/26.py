def find_digit(num, nth):
    n = str(num)
    if len(n) < nth:
        return 0
    if nth <= 0:
        return -1
    return int(n.replace('-', '0')[::-1][nth - 1])
