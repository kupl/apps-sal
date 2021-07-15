def find_digit(num, nth):
    return -1 if nth <= 0 else find_digit(-num, nth) if num < 0 else int(str(num).zfill(nth)[-nth])
