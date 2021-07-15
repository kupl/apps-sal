def find_digit(num, nth):
    if nth < 1: return -1
    n = [int(x) for x in str(abs(num))]
    return 0 if len(n) < nth else n[len(n) - nth]
