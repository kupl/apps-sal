def find_digit(num, nth):
    return int(str(abs(num)).zfill(nth)[-nth]) if nth > 0 else -1
