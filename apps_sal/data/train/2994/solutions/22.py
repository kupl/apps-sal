def find_digit(num, nth):
    if nth <= 0:
        return -1
    return int(str(abs(num)).zfill(nth)[-nth])
