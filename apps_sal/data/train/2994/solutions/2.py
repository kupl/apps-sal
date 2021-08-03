def find_digit(num, nth):
    return 0 if nth > len(str(num)) else -1 if nth <= 0 else int(str(num)[-nth])
