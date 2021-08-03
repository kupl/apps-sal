def find_digit(num, nth):
    if nth <= 0:
        return -1
    s = str(num).strip("-")
    if len(s) < nth:
        return 0
    return int(s[-nth])
