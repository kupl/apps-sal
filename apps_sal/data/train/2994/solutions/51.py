def find_digit(num, nth):
    n = str(abs(num))[::-1]
    return -1 if nth < 1 else 0 if nth > len(n) else int(n[nth-1])
