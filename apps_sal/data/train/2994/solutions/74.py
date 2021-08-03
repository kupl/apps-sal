def find_digit(num, nth):
    return int((f'{abs(num):0{nth}}'[::-1])[nth - 1]) if nth > 0 else -1
