def find_digit(num, nth):
    if nth <= 0:
        return -1
    return int([*reversed(str(num))][nth-1]) if nth < len(str(num)) + 1  else 0
