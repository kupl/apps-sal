def find_digit(num, nth):
    if nth <= 0:
        return -1
    num = str(abs(num))
    return 0 if nth > len(num) else int(num[::-1][nth - 1])
