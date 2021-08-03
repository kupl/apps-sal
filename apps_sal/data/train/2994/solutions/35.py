def find_digit(num, nth):
    s = str(num)
    if nth in range(1, len(s) + 1):
        return int(s[-nth])
    if nth == 0 or nth <= 0:
        return -1
    else:
        return 0
