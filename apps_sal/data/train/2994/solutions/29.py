def find_digit(num, nth):
    if nth <= 0: return -1
    n = str(abs(num))
    return int(n[-nth]) if nth <= len(n) else 0
