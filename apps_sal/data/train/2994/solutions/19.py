def find_digit(num, nth):
    return abs(num) % 10 ** nth // 10 ** (nth - 1) if nth > 0 else -1
