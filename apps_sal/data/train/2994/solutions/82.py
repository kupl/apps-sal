def find_digit(num, nth):
    string = str(abs(num)).zfill(nth)
    return int(string[-1 * nth]) if nth > 0 else -1
