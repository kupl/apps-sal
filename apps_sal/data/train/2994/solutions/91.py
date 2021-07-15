def find_digit(num, nth):
    num = abs(num)
    return -1 if nth < 1 else 0 if len(str(num)) < nth else int(str(num)[len(str(num)) - nth])
