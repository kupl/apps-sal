def find_digit(num, nth):
    print(num, nth)
    if nth <= 0:
        return -1
    s = str(abs(num))
    if nth > len(s):
        return 0
    return int(s[-nth])
