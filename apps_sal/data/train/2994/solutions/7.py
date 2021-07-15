def find_digit(num, nth):
    if nth < 1: return -1
    s = str(num)
    if nth > len(s): return 0
    return int(s[len(s) - nth])
