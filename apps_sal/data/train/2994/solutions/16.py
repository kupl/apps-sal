def find_digit(num, nth):
    num = str(abs(num))
    return -1 if nth <= 0 else int(num[-nth]) if len(num) >= nth else 0
