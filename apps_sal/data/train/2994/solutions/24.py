def find_digit(num, nth):
    return ~0 if nth <= 0 else (abs(num) // 10 ** (nth - 1)) % 10
