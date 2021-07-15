def find_digit(num, nth):
    return int(f'{num:0{-~nth}}'[-nth]) if nth > 0 else -1
