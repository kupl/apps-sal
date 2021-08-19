def find_digit(num, nth):
    if nth <= 0:
        return -1
    s = str(abs(num))[::-1]
    if nth > len(s):
        return 0
    return int(s[nth - 1])
